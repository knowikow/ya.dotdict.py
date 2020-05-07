import pytest

from ya.dotdict import DotDictMixin


class SimpleDict(DotDictMixin, dict):
    pass


class ComplexBaseDict(dict):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.base_attribute = 'value'

    def base_method(self):
        return 'base_method'


class ComplexBaseSlots(dict):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.base_attribute = 'value'

    def base_method(self):
        return 'base_method'


class ComplexDict(DotDictMixin, ComplexBaseDict):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.attribute = 'value'

    def method(self):
        return 'method'


class ComplexSlots(DotDictMixin, ComplexBaseSlots):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.attribute = 'value'

    def method(self):
        return 'method'


def test_dict_getitem():
    instance = SimpleDict()

    instance['foo'] = 'bar'

    assert instance['foo'] == 'bar'
    assert instance.foo == 'bar'


def test_dict_setitem():
    instance = SimpleDict()

    instance.foo = 'bar'

    assert instance['foo'] == 'bar'
    assert instance.foo == 'bar'


def test_dict_delitem():
    instance = SimpleDict()

    instance['foo'] = 'bar'

    assert instance['foo'] == 'bar'
    assert instance.foo == 'bar'

    del instance.foo

    with pytest.raises(AttributeError):
        instance.foo


# vim:et sw=4 ts=4
