django-admin-ribbon
===================

[![Build Status](https://travis-ci.org/skioo/django-admin-ribbon.svg?branch=master)](https://travis-ci.org/skioo/django-admin-ribbon)
[![PyPI version](https://badge.fury.io/py/django-admin-ribbon.svg)](https://badge.fury.io/py/django-admin-ribbon)
[![Requirements Status](https://requires.io/github/skioo/django-admin-ribbon/requirements.svg?branch=master)](https://requires.io/github/skioo/django-admin-ribbon/requirements/?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Overlays a configurable ribbon across the admin-ui, in order to differentiate between environments.

For example:

![Example ribbon](docs/admin_with_ribbon.png)

Requirements
------------

* Python: Any version
* Django: 1.8 and over

Setup
-----

Install from pip:

    pip install django-admin-ribbon
   
   
Add `'adminribbon'` to your `INSTALLED_APPS`, before `'django.contrib.admin'` (because we override their template).


    INSTALLED_APPS = (
        ...
        'adminribbon',
        'django-contrib.admin',
        ...
    )
 


Add `'adminribbon.context_processors.from_settings'` to the templates `'context_processors'`.


For each environment (usually in different settings files) configure the text and color of the ribbon, for example:

    ADMIN_RIBBON = {
        'TEXT': 'Dev',
        'COLOR': 'green',
    }


Credits
-------

Inspired by https://hackernoon.com/5-ways-to-make-django-admin-safer-eb7753698ac8
