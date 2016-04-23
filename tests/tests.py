"""Unit tests for plugout"""
import os
import unittest
from plugout import PluginManager
from plugout.examples.base import ExampleBasePlugin
from plugout.examples import sample_plugin

SAMPLE_PLUGIN_PATH = 'plugout.examples.sample_plugin.SamplePlugin'
SAMPLE_PLUGIN_PATH_CALLABLE = 'plugout.examples.sample_plugin_callable.get_plugin'
EXAMPLE_FOLDER = os.path.abspath(sample_plugin.__file__)

if EXAMPLE_FOLDER.endswith('.pyc'):
    EXAMPLE_FOLDER = EXAMPLE_FOLDER[:-1]


class PlugoutTests(unittest.TestCase):

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
