# auth: Flynn Wang
# date: 28/12/22
# desc:
import logging
import random


def get_svn_version(component_name) -> str:
    """Get svn version number as a string from SVN server.
    Just return a random number to be simplified.
    Here we are going to use the svn library and get server configurations from settings.

    Args:
        component_name: used as part of SVN path

    Returns: the svn version number of specific component

    """
    version = random.randint(1000, 10000)
    logging.debug(f'get svn version number of component {component_name} version {version}')
    return f'{version}'
