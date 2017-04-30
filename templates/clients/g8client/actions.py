from js9 import j


def input(job):
    args = job.model.args
    if "account" not in args or args["account"].strip() == "":
        args['account'] = args["login"]

    login = args.get('login', '')
    password = args.get('password', '')
    jwt = args.get('jwt', '')
    if login == '' and password == '' and jwt == '':
        raise j.exceptions.Input("Either username/password or jwt should be entered for %s" % job.service)

    return args


def processChange(job):
    service = job.service
    args = job.model.args
    category = args.pop('changeCategory')
    if category == 'dataschema':
        for key, value in args.items():
            setattr(service.model.data, key, value)
    service.save()
