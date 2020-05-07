from collections import defaultdict
from collections.abc import MutableMapping


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


class DotDictWrapper(DotDictMixin, MutableMapping):
    """A wrapper class for providing attribute access to dict-like objects."""


class DotDict(DotDictMixin, dict):
    """Standard dictionary with attribute access."""


class DotDefaultDict(DotDictMixin, defaultdict):
    """Standard defaultdict with attribute access."""


# vim:et sw=4 ts=4