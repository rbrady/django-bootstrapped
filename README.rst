====================
Django Bootstrapped
====================

Bootstrapped is a reusable Django application to quickly integrate the Bootstrap toolkit from Twitter.  It's a
collection of the bootstrap toolkit files and template tags to display them.

This application depends on django.contrib.staticfiles.

No files from Twitter's Bootstrap toolkit have been modified and retain their Apache 2.0 license.

* Note: This app only works on Django 1.3 and newer.

Installation
============

pip install django-bootstrapped


Configuration
=============

#. Add the `bootstrapped` directory to your Python path.

#. Ensure `django.contrib.staticfiles` is added to your `INSTALLED_APPS` setting.

#. Ensure `django.contrib.staticfiles` is configured properly.

#. Add `bootstrapped` to your `INSTALLED_APPS` setting.

#. Run `manage.py collectstatic` to copy the Twitter Bootstrap toolkit files to your static directory.


Template Usage
=================
This application exposes a few template tags for including the Bootstrap toolkit files.

Load the template tags before usage::
    {% load bootstrap %}

TODO: Explain each template tag and all permutations.



TODO: Explain how to customize/override using less.