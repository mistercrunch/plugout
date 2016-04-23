# Plugout

Plugout is the simplest plugin manager for Python.

Given a BasePlugin provided by your app

    class BaseSuperPlugin(object):
        pass

Provided a derivative added externally to your app

    from yourapp.pluginmanager import BaseSuperPlugin

    class MySuperPluginI(BaseSuperPlugin):
        pass

Now given discover the plugins from your app, using a dotted notation to
the package.module.ClassName:

    from plugout import PluginManager
    from yourapp.pluginmanager import BaseSuperPlugin

    pm = PluginManager(base_class=BaseSuperPlugin)
    pm.load_from_dotted_paths(['yourapp_plguins.file_above.MySuperPlugin'])
    pm.plugins  # A list of plugins classes

You can also crawl through a folder/subfolders to discover derivatives of
BaseSuperPlugin

    pm.load_from_filepath('/usr/lib/share/super_plugins/')

In some cases, importing plugins can lead to circular dependencies, in that
case you can reference a dotted object reference to a callable

    pm.load_from_callables(['yourapp_plguins.file_above.get_my_plugin'])
