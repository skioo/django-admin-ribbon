#!/usr/bin/env python
from setuptools import setup

import adminribbon

setup(
    name='django-admin-ribbon',
    version=adminribbon.__version__,
    description='Quickly differentiate django environments',
    long_description='',
    author='Nicholas Wolff',
    author_email='nwolff@gmail.com',
    url=adminribbon.__URL__,
    download_url='https://pypi.python.org/pypi/django-admin-ribbon',
    packages=[
        'adminribbon',
    ],
    package_data={'adminribbon': [
        'templates/admin/base_site.html',
    ]},
    install_requires=[
        'Django>=1.8',
    ],
    license=adminribbon.__licence__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
