"""Defines a simple example plugin to be use for reference and in unit tests"""


class ExampleBasePlugin(object):
    """A very simple example of a plugin's base class"""

    @staticmethod
    def get_hello():
        return "Hello"
