"""Sample of a plugin that is defined and returned in a callable"""


def get_plugin(base_class):


    class SamplePlugin(base_class):

        """Implements a sample plugin by deriving ExampleBasePlugin"""

        @staticmethod
        def get_world():
            return "world"

    return SamplePlugin
