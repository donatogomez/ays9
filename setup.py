from distutils.core import setup

setup(
    name='JumpScale9AYS',
    version='9.0.0a1',
    description='Automation framework for cloud workloads ays lib',
    url='https://github.com/Jumpscale/ays9',
    author='GreenItGlobe',
    author_email='info@gig.tech',
    license='Apache',
    packages=['JumpScale9AYS'],
    install_requires=[
        'g8core',
        'sanic>=0.5.2',
        'jsonschema',
        'python-jose'
    ],
    scripts=['cmds/ays']
)
