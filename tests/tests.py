"""Unit tests for extend"""
import os
import unittest
from extend import PluginManager
from extend.examples.base import ExampleBasePlugin
from extend.examples import sample_plugin

SAMPLE_PLUGIN_PATH = 'extend.examples.sample_plugin.SamplePlugin'
SAMPLE_PLUGIN_PATH_CALLABLE = 'extend.examples.sample_plugin_callable.get_plugin'
EXAMPLE_FOLDER = os.path.dirname(sample_plugin.__file__)


class ExtendTests(unittest.TestCase):

    def _hello(self, hw_plugin):
        assert "Hello world" == hw_plugin.get_hello() + " " + hw_plugin.get_world()

    def test_dotted(self):
        pm = PluginManager(ExampleBasePlugin)
        pm.load_from_dotted_paths([SAMPLE_PLUGIN_PATH])
        assert len(pm.plugins) == 1
        self._hello(pm.plugins[0])

    def test_os_walk(self):
        pm = PluginManager(ExampleBasePlugin)
        pm.load_from_filepath(EXAMPLE_FOLDER)
        assert len(pm.plugins) >= 1
        self._hello(pm.plugins[0])

    def test_from_callable(self):
        pm = PluginManager(ExampleBasePlugin)
        pm.load_from_callables([SAMPLE_PLUGIN_PATH_CALLABLE])
        print(pm.plugins)
        assert len(pm.plugins) == 1
        self._hello(pm.plugins[0])

    def test_bad_calls(self):
        pm = PluginManager(ExampleBasePlugin)
        pm.load_from_dotted_paths(['dev.null'])
        assert len(pm.plugins) == 0

        pm = PluginManager(ExampleBasePlugin)
        pm.load_from_dotted_paths(['sys.path'])
        assert len(pm.plugins) == 0

        pm = PluginManager(ExampleBasePlugin)
        pm.load_from_callables(['dev.null'])
        assert len(pm.plugins) == 0



if __name__ == '__main__':
    unittest.main()
