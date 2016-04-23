"""Sample of a plugin that is defined and returned in a callable"""

def get_plugin():
    from plugout.examples.base import ExampleBasePlugin


    class SamplePlugin(ExampleBasePlugin):

        """Implements a sample plugin by deriving ExampleBasePlugin"""

        @staticmethod
        def get_world():
            return "world"
    return SamplePlugin
