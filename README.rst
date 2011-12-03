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

`bootstrap_css`

This tag renders the link tag for the bootstrap.min.css file.  It will render the un-minified version if
settings.TEMPLATE_DEBUG is set to True.::

    {% bootstrap_css %}

Output::

    <link rel="stylesheet" type="text/css" href="/static/bootstrap.css">

`bootstrap_js`

The Bootstrap toolkit provides some javascript love (http://twitter.github.com/bootstrap/#javascript) that is
compatible with jQuery and Ender.  This tag renders the appropriate script include tag for each plugin defined.

    {% bootstrap_js modal alerts dropdown %}

Output::

    <script src="bootstrap-alerts.js" type="text/javascript"></script>
    <script src="bootstrap-dropdown.js" type="text/javascript"></script>
    <script src="bootstrap-modal.js" type="text/javascript"></script>





TODO: Explain how to customize/override using less.