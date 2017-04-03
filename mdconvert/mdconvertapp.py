from jupyter_core.application import JupyterApp, base_aliases
from traitlets import CUnicode

# Add additional command line aliases
aliases = dict(base_aliases)


class MDConvertApp(JupyterApp):
    # Enable some command line shortcuts
    aliases = aliases
    files = CUnicode(config=True)

    def initialize(self, argv=None):
        super(MDConvertApp, self).initialize(argv)

    def start(self):
        super(MDConvertApp, self).start()


launch_instance = MDConvertApp.launch_instance
