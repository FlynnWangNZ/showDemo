# auth: Flynn Wang
# date: 28/12/22
# desc:
import random


def get_svn_version(component_index) -> str:
    """Get svn version number as a string from SVN server.
    Just return a random number to be simplified.
    Here we are going to use the svn library and get server configurations from settings.

    Args:
        component_index: used as part of SVN path

    Returns: the svn version number of specific component

    """
    return f'{component_index}{random.randint(1000, 10000)}'
