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

```bootstrap_css```

This tag renders the link tag for the bootstrap.min.css file.  It will render the un-minified version if
settings.TEMPLATE_DEBUG is set to True.::

    {% bootstrap_css %}

Output::

    <link rel="stylesheet" type="text/css" href="/static/bootstrap.css">

```bootstrap_js```

The Bootstrap toolkit provides some javascript love (http://twitter.github.com/bootstrap/#javascript) that is
compatible with jQuery and Ender.  This tag renders the appropriate script include tag for each plugin defined.  The tag
does not include jQuery or Ender, that's up to you.

    {% bootstrap_js modal alerts dropdown %}

Output::

    <script src="bootstrap-alerts.js" type="text/javascript"></script>
    <script src="bootstrap-dropdown.js" type="text/javascript"></script>
    <script src="bootstrap-modal.js" type="text/javascript"></script>

* Note: The popover javascript file has a dependency on the twipsy file.  If you add popover to the list and forget to add twipsy, the tag will do it for you.

Alternatively, you may just want to include all of the scripts.  If so, just use `all` for the tag arguments.:

    {% bootstrap_js all %}



```bootstrap_custom_less```

You may want to customize the output of the bootstrap.css using Less (http://lesscss.org/).  Bootstrap was built from
Preboot, an open-source pack of mixins and variables to be used in conjunction with Less, a CSS preprocessor for faster
and easier web development.  This tag accepts an argument for a file path somewhere in your /static/ root directory and
outputs a script tag for it.:

    {% bootstrap_custom_less "lib/bootstrap_custom.less" %}

Output::

    <link rel="stylesheet/less" type="text/css" href="/static/lib/bootstrap_custom.less" media="all">
    <script src="/static/js/less-1.1.5.min.js" type="text/javascript"></script>
