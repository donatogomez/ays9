from distutils.core import setup

setup(
    name='JumpScaleAYS',
    version='9.0.0a1',
    description='Automation framework for cloud workloads ays lib',
    url='https://github.com/Jumpscale/ays9',
    author='GreenItGlobe',
    author_email='info@gig.tech',
    license='Apache',
    packages=['JumpScaleAYS'],
    install_requires=[
        'redis',
        'colorlog',
        'pytoml',
        'ipython',
        'colored_traceback',
        'pystache',
        'libtmux',
        'httplib2',
        'netaddr'
    ]
)
