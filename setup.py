from setuptools import setup
from setuptools.command.install import install as _install
from setuptools.command.develop import develop as _develop
import os


def _post_install(libname, libpath):
    from js9 import j

    # add this plugin to the config
    c = j.core.state.configGet('plugins', defval={})
    c[libname] = libpath
    j.core.state.configSet('plugins', c)

    print("****:%s:%s" % (libname, libpath))

    j.tools.jsloader.generatePlugins()
    j.tools.jsloader.copyPyLibs()


class install(_install):

    def run(self):
        _install.run(self)
        libname = self.config_vars['dist_name']
        libpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), libname)
        self.execute(_post_install, (libname, libpath), msg="Running post install task")


class develop(_develop):

    def run(self):
        _develop.run(self)
        libname = self.config_vars['dist_name']
        libpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), libname)
        self.execute(_post_install, (libname, libpath), msg="Running post install task")


setup(
    name='JumpScale9AYS',
    version='9.0.0',
    description='Automation framework for cloud workloads ays lib',
    url='https://github.com/Jumpscale/ays9',
    author='GreenItGlobe',
    author_email='info@gig.tech',
    license='Apache',
    packages=['JumpScale9AYS'],
    install_requires=[
        'JumpScale9>=9.0.0',
        'JumpScale9Lib>=9.0.0',
        'g8core>=1.0.0',  # is not ok, because strictly spoken this is not part of ays9
        'jsonschema>=2.6.0',
        'python-jose>=1.3.2',
        'sanic>=0.5.2',
        'git+https://github.com/gigforks/PyInotify',
    ],
    cmdclass={
        'install': install,
        'develop': develop,
        'developement': develop
    },
    scripts=['cmds/ays'],
)
