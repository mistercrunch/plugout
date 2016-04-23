"""Base module for plugout"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import inspect
import imp
import logging
import os
from pydoc import locate
import re


class PluginManager(object):

    """Loads and exposes plugins"""

    def __init__(self, base_class=object):
        """
        :param base_class: The base class that plugins are plugouting
        :type base_class: object
        """
        self.base_class = base_class
        self.plugins = []

    @staticmethod
    def locate_or_raise(path):
        obj = locate(path)
        if not obj:
            raise ImportError("Could not locate {}".format(path))
        return obj

    def _add_plugin(self, candidate):
        """Validates the plugin is a derivate of the base plugin class before adding it"""
        if self._is_plugin(candidate):
            logging.info("Loaded plugin {}".format(candidate))
            if candidate not in self.plugins:
                self.plugins.append(candidate)
        else:
            logging.error("{} isn't a subclass of {}".format(
                candidate, self.base_class))

    def _is_plugin(self, candidate):
        """Check whether the object is a plugin"""
        return (
            inspect.isclass(candidate) and
            issubclass(candidate, self.base_class)
        )

    def load_from_dotted_paths(self, path_list):
        """Loads plugins from a list of dotted paths

        :param path_list: A list of dotted python references as in
        ``['package1.package2.module1.ClassName']``
        :type path_list: list
        """
        for path in path_list:
            try:
                plugin = self.locate_or_raise(path)
            except Exception as e:
                logging.error("Couldn't load {}".format(path))
                logging.exception(e)
            else:
                self._add_plugin(plugin)

    def load_from_callables(self, callable_path_list):
        """Loads plugins from a list of callables

        :param callables: A list of Python callables (functions or methods)
            that are expected to return plugin classes
        :type path_list: list
        """
        for path in callable_path_list:
            try:
                f = self.locate_or_raise(path)
            except Exception as e:
                logging.error("Couldn't load {}".format(path))
                logging.exception(e)
            else:
                if hasattr(f, '__call__'):
                    plugin = f()
                    self._add_plugin(plugin)
                else:
                    logging.error("{} doesn't appear to be callable".format(f))

    def load_from_filepath(self, path_reference, followlinks=True):
        """Loads from an OS filepath

        The process will recurse through the folder and import python files,
        introspect them, and find derivatives of your plugin's base class.

        :param path_reference: An os folder or filepath reference for the
            process to search into
        :type path_reference: str
        """
        norm_pattern = re.compile(r'[/|.]')
        def process_file(filepath):
            mod_name, file_ext = os.path.splitext(
                os.path.split(filepath)[-1])
            if file_ext != '.py':
                return

            # normalize root path as namespace
            namespace = '_'.join([
                re.sub(norm_pattern, '__', os.path.dirname(filepath)), mod_name])

            m = imp.load_source(namespace, filepath)
            for obj in list(m.__dict__.values()):
                if self._is_plugin(obj):
                    self._add_plugin(obj)

        if os.path.isfile(path_reference):
            process_file(path_reference)
            return

        for root, dirs, files in os.walk(
                path_reference, followlinks=followlinks):
            for f in files:
                try:
                    filepath = os.path.join(root, f)
                    if not os.path.isfile(filepath):
                        continue
                    else:
                        process_file(filepath)
                except Exception as e:
                    logging.exception(e)
                    logging.error('Failed to import plugin {}'.format(filepath))
