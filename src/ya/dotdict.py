
class DotDictMixin:
    """A mixin class for providing attribute access to dict-like classes."""
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError as ex:
            raise AttributeError(name) from ex

    def __setattr__(self, name, value):
        if name in super().__dir__():
            super().__setattr__(name, value)
        else:
            self[name] = value

    def __delattr__(self, name):
        try:
            super().__delattr__(name)
        except AttributeError:
            del self[name]


class DotDict(DotDictMixin, dict):
    """Standard dictionary with attribute access.

    >>> d = DotDict()
    >>> d['spam'] = 'eggs'
    >>> d.spam
    'eggs'
    >>> d.spam = 100
    >>> d['spam']
    100
    """
    def __init__(self,  default_factory=None, **kwds):
        super().__init__(**kwds)
        self._default_factory = default_factory


# vim:et sw=4 ts=4
