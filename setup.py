from setuptools import setup

setup(
    name='RobopolyAPI',
    version='0.1',
    long_description=__doc__,
    packages=['api'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=0.2',
        'python-ldap>=0.2'
    ]
)
