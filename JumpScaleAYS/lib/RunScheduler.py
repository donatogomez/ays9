import asyncio
from JumpScale import j

NORMAL_RUN_PRIORITY = 1
ERROR_RUN_PRIORITY = 10


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
        self._loop = repo._loop
        self.queue = asyncio.PriorityQueue(maxsize=0)
        self.is_running = False

    async def start(self):
        self.logger.info("{} started".format(self))
        if self.is_running:
            return

        self.is_running = True
        while self.is_running:
            _, run = await self.queue.get()
            if not self.is_running:
                break

            try:
                await run.execute()
            finally:
                self.queue.task_done()

        self.logger.info("{} stopped".format(self))

    async def stop(self, timeout=30):
        self.is_running = False
        self.logger.info("{} stopping...".format(self))
        try:
            await asyncio.wait_for(self.queue.join(), timeout=timeout, loop=self._loop)
        except asyncio.TimeoutError:
            self.logger.warning("stop timeout reach for {}. possible run interrupted".format(self))

    async def add(self, run):
        """
        add a run to the queue of run to be executed
        """
        if not self.is_running:
            raise j.exceptions.RuntimeError("Trying to add a run to a stopped run scheduler ({})".format(self))

        self.logger.debug("add run {} to {}".format(run.model.key, self))
        await self.queue.put((NORMAL_RUN_PRIORITY, run))

    def __repr__(self):
        return "RunScheduler<{}>".format(self.repo.name)

#
# async def main(repo):
#     scheduler = RunScheduler(repo, repo._loop)
#     asyncio.ensure_future(scheduler.start())
#
#     run = repo.runCreate()
#     await scheduler.add(run)
#     await scheduler.stop()
#
# if __name__ == '__main__':
#     from JumpScale import j
#     j.atyourservice._start()
#     repo = j.atyourservice.aysRepos.get('/opt/code/cockpit_repos/grid')
#     repo._loop.run_until_complete(main(repo))
#     from IPython import embed;embed()
