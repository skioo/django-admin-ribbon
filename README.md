django-admin-ribbon
===================

[![Build Status](https://travis-ci.org/skioo/django-admin-ribbon.svg?branch=master)](https://travis-ci.org/skioo/django-admin-ribbon)


Overlays a configurable ribbon across the admin-ui, in order to differentiate between environments.
For example:

![Example ribbon](docs/admin_with_ribbon.png)

Requirements
------------

* **Python**: any version
* **Django**: any version


Installation
------------

- Add `'adminribbon'` to your `INSTALLED_APPS`, before `'django.contrib.admin'` (because we override their template).
- Add `'adminribbon.context_processors.from_settings'` to the templates `'context_processors'`.
- For each environment (usually in different settings files) configure the text and color
of the ribbon, for example:

```
ADMIN_RIBBON = {
    'TEXT': 'dev',
    'COLOR': 'green',
}
```



To work on this code
--------------------

    pip install -e .

To run tests:

    tox

To release a version to pypi:
- Edit \_\_version\_\_ in \_\_init\_\_.py
- Push and wait for the build to succeed
- Create a release in github, travis will build and deploy the new version to pypi: https://pypi.python.org/pypi/django-admin-ribbon
