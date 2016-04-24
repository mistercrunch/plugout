[![Build Status](https://travis-ci.org/mistercrunch/plugout.svg?branch=master)](https://travis-ci.org/mistercrunch/plugout)
[![PyPI](https://img.shields.io/pypi/pyversions/plugout.svg?maxAge=2592000)](https://pypi.python.org/pypi/plugout)
[![PyPI](https://img.shields.io/pypi/v/plugout.svg?maxAge=2592000)](https://pypi.python.org/pypi/plugout)
[![Code Health](https://landscape.io/github/mistercrunch/plugout/master/landscape.svg?style=flat)](https://landscape.io/github/mistercrunch/plugout/master)
[![Coverage Status](https://coveralls.io/repos/github/mistercrunch/plugout/badge.svg?branch=master)](https://coveralls.io/github/mistercrunch/plugout?branch=master)


# PlugOut

Plugout is a plugin manager for Python.

It's a common pattern to allow people to extend an application with plugins.
Plugout lets you define a base class that can be derived looped back into
your application.

Plugout was originally designed to allow visualization extensions to
[Caravel](github.com/airbnb/caravel) and plugins for
[Airflow](github.com/airbnb/airflow).


## Example

Now picture an application for image processing `shotophot` that can be
extended with filter

    class BaseFilterPlugin(object):
        def process(img):
            raise NotImplemented()

Now picture and external module that defines a filter

    from shotophot import BaseFilterPlugin

    class BlackWhitePlugin(BaseFilterPlugin):
        def process(img):
            return mutate(img)

Now your application can discover the objects provided externally.

    from plugout import PluginManager
    from shotophot import BaseFilterPlugin
    from shotophot import conf

    # Load a plugout plugin manager specifying the base class we are
    # looking for derivatives from
    pm = PluginManager(base_class=BaseSuperPlugin)

    # where conf.get('PLUGIN_PATHS') is a user provided list of Python
    # dotted reference as in `['package.module.ClassName']`, where
    # ClassName is a derivative of BaseFilterPlugin
    pm.load_from_dotted_paths(conf.get('PLUGIN_PATHS'))

    pm.plugins  # A list of plugins classes that were found

You can also crawl through a folder/subfolders to discover derivatives of
BaseSuperPlugin

    # where conf.get('PLUGINS_FOLDER') is a file system reference
    # as in `/var/lib/share/shotophot_plugins`
    pm.load_from_filepath(conf.get('PLUGINS_FOLDER'))

In some cases, importing plugins can lead to circular dependencies, in that
case you can reference a dotted object reference to a callable

    # where conf.get('PLUGIN_CALLABLES') is a dotted Python reference to
    # callables expected to return a derivative of BaseFilterPlugin
    # Note that the callable you define will be passed base_class as the first
    # argument
    pm.load_from_callables(conf.get('PLUGIN_CALLABLES'))
