"""
This type stub file was generated by pyright.
"""

class requires_geos:
    def __init__(self, version) -> None:
        ...
    
    def __call__(self, func): # -> _Wrapped[(...), Unknown, (*args: Unknown, **kwargs: Unknown), Unknown]:
        ...
    


def multithreading_enabled(func): # -> _Wrapped[(...), Unknown, (*args: Unknown, **kwargs: Unknown), Unknown]:
    """Prepare multithreading by setting the writable flags of object type
    ndarrays to False.

    NB: multithreading also requires the GIL to be released, which is done in
    the C extension (ufuncs.c)."""
    ...

