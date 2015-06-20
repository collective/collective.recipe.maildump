collective.recipe.maildump
==========================

.. contents::

Introduction
------------

This recipe installs `maildump <https://github.com/ThiefMaster/maildump>`_  a
python-based clone of the awesome `MailCatcher <https://github.com/sj26/mailcatcher>`_
tool.

Installation
------------

Look at this example::

    [buildout]
    parts = maildump

    [maildump]
    recipe = collective.recipe.maildump

That's all.

How to use it
-------------

Just run ``bin/maildumpctl``. By default it will start the web server on port
``1080`` and the smtp server on port ``1025``.

Image maildump running with no commands.

