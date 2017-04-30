def init(job):
    service = job.service
    if service.model.data.type.upper() not in ["D", "B"]:
        raise j.exceptions.Input("disk.ovc's type must be data (D) or boot (B) only")
