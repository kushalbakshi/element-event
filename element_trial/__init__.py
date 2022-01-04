__author__ = "DataJoint"
__date__ = "December, 2021"
__version__ = "0.1.0c0"

__all__ = ['__author__', '__version__', '__date__']

import datajoint as dj
dj.config['enable_python_native_blobs'] = True

"""
Two schemas, trial and event. Trial for fully trialized, segmented.
Event for events independent of trials, like an act of naturaistic behavior.
"""
