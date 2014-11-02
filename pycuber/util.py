"""
Utilities
"""

class FrozenDict(dict):

    __doc__ = dict.__doc__

    def _delattr(func):
        def EmptyAttribute(self, *args, **kwargs):
            raise AttributeError(
                "'FrozenDict' object has no attribute '{0}'"
                .format(func.__name__)
                )
        return EmptyAttribute

    @_delattr
    def __setitem__(): pass
    @_delattr
    def __delitem__(): pass
    @_delattr
    def clear(): pass
    @_delattr
    def pop(): pass
    @_delattr
    def popitem(): pass
    @_delattr
    def setdefault(): pass
    @_delattr
    def update(): pass

    del _delattr

