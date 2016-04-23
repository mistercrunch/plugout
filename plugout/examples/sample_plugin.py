from plugout.examples.base import ExampleBasePlugin

class SamplePlugin(ExampleBasePlugin):

    """Implements a sample plugin by deriving ExampleBasePlugin"""

    @staticmethod
    def get_world():
        return "world"
