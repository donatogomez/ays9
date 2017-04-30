import asyncio
from js9 import j

NORMAL_RUN_PRIORITY = 1
ERROR_RUN_PRIORITY = 10

RETRY_DELAY = {
    1: 10,  # 30sec
    2: 60,  # 1min
    3: 300,  # 5min
    4: 600,  # 10min
    5: 1800,  # 30min
    6: 1800,  # 30min
}  # total: 1h 16min 30sec


class RunScheduler:
    """
    This class is reponsible to execte the run requested by the users
    as well as the automatic error runs

    Since only one can be executed at a time, all the run are pushed on a PriorityQueue.
    Requested runs have always hightest priority over error runs.
    """

    def __init__(self, repo):
        self.logger = j.logger.get("j.ays.RunScheduler")
        self.repo = repo
        self.queue = asyncio.PriorityQueue(maxsize=0)
        self._retries = []
        self._retries_lock = asyncio.Lock()
        self._accept = False
        self.is_running = False

    async def start(self):
        """
        starts the run scheduler and begin whating the run queue.
        """
        self.logger.info("{} started".format(self))
        if self.is_running:
            return

        self.is_running = True
        self._accept = True
        while self.is_running:

            try:
                _, run = await asyncio.wait_for(self.queue.get(), timeout=10)
            except asyncio.TimeoutError:
                # this allow to exit the loop when stopped is asked.
                # without the timeout the queue.get blocks forever
                if not self._accept:
                    break
                continue

            try:
                await run.execute()
            except:
                # exception is handle in the job directly,
                # catch here to not interrupt the loop
                pass
            finally:
                self.queue.task_done()

        self.is_running = False
        self.logger.info("{} stopped".format(self))

    async def stop(self, timeout=30):
        """
        stops the run scheduler
        When the run scheduler is stopped you can't add send new run to it
        @param timout: number of second we wait for the current run to finish before force stopping execution.

        """
        self._accept = False
        self.logger.info("{} stopping...".format(self))

        try:
            # wait for runs in the queue and all retries actions
            with await self._retries_lock:
                for retry in self._retries:
                    retry.cancel()
            to_wait = [self.queue.join(), *self._retries]
            await asyncio.wait(to_wait, timeout=timeout, loop=self.repo._loop)

        except asyncio.TimeoutError:
            self.logger.warning("stop timeout reach for {}. possible run interrupted".format(self))

        self._retries = []

    async def add(self, run, priority=NORMAL_RUN_PRIORITY):
        """
        add a run to the queue of run to be executed
        @param priority: one of NORMAL_RUN_PRIORITY or ERROR_RUN_PRIORITY
                         runs added with NORMAL_RUN_PRIORITY will always be executed before
                         the ones added with ERROR_RUN_PRIORITY
        """
        if priority not in [NORMAL_RUN_PRIORITY, ERROR_RUN_PRIORITY]:
            raise j.exceptions.Input("priority should {} or {}, {} given".format(
                             NORMAL_RUN_PRIORITY,
                             ERROR_RUN_PRIORITY,
                             priority))

        if not self._accept:
            raise j.exceptions.RuntimeError("{} is stopping, can't add new run to it".format(self))

        self.logger.debug("add run {} to {}".format(run.model.key, self))
        await self.queue.put((priority, run))

    async def retry(self, service, action_name):
        """
        Retry to executed a failed job from a run.
        The job will be rescheduled with increasing delay till it succeed or its error level reach 7.
        @param service: service object
        @param action_name: name of the action to retry
        """
        async def do_retry(service, action_name):

            service_key = service.model.key
            action = service.model.actions[action_name]

            if action.state != 'error':
                self.logger.info("no need to retry action {}, state not error".format(action))
                return

            if list(RETRY_DELAY.keys())[-1] < action.errorNr:
                self.logger.info("action {} reached max retry, not rescheduling again.".format(action))
                return

            delay = RETRY_DELAY[action.errorNr]
            # make sure we don't reschedule with a delay smaller then the timeout of the job
            if action.timeout > 0 and action.timeout > delay:
                delay = action.timeout
            self.logger.info("reschedule {} from {} in {}sec".format(action_name, service, delay))

            await asyncio.sleep(delay)

            # make sure the service has not been deleted while we were waiting
            try:
                service = self.repo.serviceGet(key=service_key)
            except j.exceptions.NotFound:
                self.logger.info("don't retry service ({}) has been deleted".format(service_key))
                return

            # make sure the action is still in error state before rescheduling it
            action = service.model.actions[action_name]
            if action.state != 'error':
                self.logger.info("don't retry action {} not in error state anymore".format(action_name))
                return

            # sending this action to the run queue
            run = self.repo.runCreate({service: [[action_name]]})
            self.logger.debug("add error run {} to {}".format(run.model.key, self))
            await self.repo.run_scheduler.add(run, ERROR_RUN_PRIORITY)

            # remove this task from the retries list
            with await self._retries_lock:
                current_task = asyncio.Task.current_task()
                if current_task in self._retries:
                    self._retries.remove(current_task)

        # add the rery to the event loop
        with await self._retries_lock:
            self._retries.append(asyncio.ensure_future(do_retry(service, action_name)))

    def __repr__(self):
        return "RunScheduler<{}>".format(self.repo.name)
