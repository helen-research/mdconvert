from .mdconvertapp import launch_instance, metadata_magic  # noqa
from ._version import __version__  # noqa

from IPython import get_ipython
get_ipython().register_magic_function(metadata_magic, magic_kind='line_cell', magic_name='metadata')
