"""
This type stub file was generated by pyright.
"""

from enum import Enum

__all__ = ["show"]
_built_with_meson = ...
class DisplayModes(Enum):
    stdout = ...
    dicts = ...


CONFIG = ...
def show(mode=...): # -> dict[str, Unknown] | None:
    """
    Show libraries and system information on which SciPy was built
    and is being used

    Parameters
    ----------
    mode : {`'stdout'`, `'dicts'`}, optional.
        Indicates how to display the config information.
        `'stdout'` prints to console, `'dicts'` returns a dictionary
        of the configuration.

    Returns
    -------
    out : {`dict`, `None`}
        If mode is `'dicts'`, a dict is returned, else None

    Notes
    -----
    1. The `'stdout'` mode will give more readable
       output if ``pyyaml`` is installed

    """
    ...

