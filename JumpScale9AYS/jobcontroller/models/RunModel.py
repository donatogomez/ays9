from js9 import j
from JumpScale9AYS.jobcontroller.Run import Run

from JumpScale9.data.capnp.ModelBase import ModelBase


class RunModel(ModelBase):
    """
    is state object for Run
    """

    def index(self):
        # put indexes in db as specified
        ind = "%s:%s" % (self.dbobj.state, self.dbobj.lastModDate)
        idx_list = self.collection._index.list(returnIndex=True)
        matched_idx = [item for item in idx_list if item[1] == self.key]
        if matched_idx:
            #  if the key exists first pop it and add the correct one
            item = matched_idx[0]
            self.collection._index.index_remove(item[0])
        self.collection._index.index({ind: self.key})

    def stepNew(self):
        step = self.collection.capnp_schema.RunStep.new_message()
        self.addSubItem('steps', step)
        return step

    def jobNew(self, xstep):
        if len(xstep.jobs) == 0:
            xstep.jobs = xstep.init_resizable_list('jobs')
        # job = self.collection.capnp_schema.RunStep.Job.new_message()
        # self.addSubItem('jobs', job)
        # return job

    @property
    def logs(self):
        logs = list()
        steps = [item.to_dict() for item in self.dbobj.steps]
        steps_with_errors = [step for step in steps if step['state'] == 'error']
        jobs = [job for step in steps_with_errors for job in step['jobs']]
        for job in jobs:
            job_model = j.core.jobcontroller.db.jobs.get(job['key'])
            logs.extend(job_model.dictFiltered['logs'])

        return logs

    def delete(self):
        # delete actual model object
        if self.collection._db.exists(self.key):
            idx = str(self.dbobj.state) + ':' + str(self.dbobj.lastModDate)
            self.collection._index.index_remove(keys=idx)
            self.collection._db.delete(self.key)

    def objectGet(self):
        return Run(model=self)

    # def __repr__(self):
    #     out = ""
    #     for item in self.methodslist:
    #         out += "%s\n" % item
    #     return out

    # __str__ = __repr__
