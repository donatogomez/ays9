def init_actions_(service, args):
    action_required = args.get('action_required')

    # don't try to install user ask to uninstall
    if action_required == 'uninstall':
        service.model.actions['install'].state = 'new'

    # don't try to uninstall user ask to install
    if action_required == 'install':
        service.model.actions['uninstall'].state = 'new'

    service.save()

    return {
        'init': [],
        'install': ['init'],
        'uninstall': [],
    }

def install(job):
    cuisine = job.service.executor.cuisine
    data = job.service.model.data

    cuisine.systemservices.kvm.disks.download_image(url=data.url, overwrite=data.overwrite)

    job.service.model.actions['uninstall'].state = 'new'
    job.service.saveAll()

def uninstall(job):
    cuisine = job.service.executor.cuisine
    data = job.service.model.data
    name = data.url.split('/')[-1]
    path = cuisine.systemservices.kvm.image_get_path(name)
    cuisine.core.file_unlink(path)

    job.service.model.actions['install'].state = 'new'
    job.service.saveAll()

def processChange(job):
    args = job.model.args
    category = args.pop('changeCategory')

    if category == 'dataschema':
        # update data model
        data = job.service.model.data

        data.overwrite = args.get('overwrite', False)

        if 'url' not in args or args['url'] == '':
            raise j.exceptions.Input("url argument cannot be empty")
        data.url = args['url']

        job.service.saveAll()
