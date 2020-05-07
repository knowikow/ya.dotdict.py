import pytest

from ya.dotdict import DotDefaultDict, DotDict, DotDictMixin, DotDictWrapper


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


class ComplexWithSlots(DotDictMixin, ComplexBaseSlots):
    __slots__ = 'attribute'.split()

    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.attribute = 'value'

    def method(self):
        return 'result'


def test_dotdict():
    instance = DotDict()

    with pytest.raises(AttributeError):
        instance.foo

    instance['foo'] = 'spam'
    assert instance['foo'] == 'spam'
    assert instance.foo == 'spam'

    instance.foo = 'eggs'
    assert instance['foo'] == 'eggs'
    assert instance.foo == 'eggs'

    del instance.foo
    with pytest.raises(AttributeError):
        instance.foo


def test_slotdict():
    instance = ComplexWithSlots()

    instance.foo = 'bar'

    assert instance['foo'] == 'bar'
    assert instance.foo == 'bar'

    with pytest.raises(KeyError):
        instance['attribute']
    assert instance.attribute == 'value'

    instance.attribute = 22
    assert instance.attribute == 22
    with pytest.raises(KeyError):
        instance['attribute']

    assert instance.method() == 'result'


def test_defaultdict():
    instance = DotDefaultDict(lambda: 'eggs')
    assert instance.spam == 'eggs'


# vim:et sw=4 ts=4
