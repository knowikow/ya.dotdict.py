.. image:: https://github.com/knowikow/ya.dotdict.py/workflows/build/badge.svg
   :target: https://github.com/knowikow/ya.dotdict.py/workflows/build/badge.svg

===================
Yet Another DotDict
===================

A Python library providing attribute access for dictionaries.
The library provides these classes:

- ``ya.dotdict.DotDict`` as a replacement for ``dict``
- ``ya.dotdict.DotDefaultDict`` as a replacement for ``collections.defaultdict``
- ``ya.dotdict.DotDictMixin``: a mixin class that can be used to add attribute-style access to any dict-like class.
  ``ya.dotdict.DotDict`` and ``ya.dotdict.DotDefaultDict`` are both implemented in terms of this mixin class

All the code examples assume ``from ya.dotdict import *``.

::

    >>> from ya.dotdict import *

``DotDict``
===========

``DotDict`` can be used as a replacement for ``dict``::

    >>> d = DotDict()
    >>> d['spam'] = 'eggs'
    >>> d.spam
    'eggs'
    >>> d.spam = 100
    >>> d['spam']
    100


``DotDefaultDict``
==================

``DotDict`` can be used as a replacement for ``defaultict``::

    >>> d = DotDefaultDict(lambda: 'eggs')
    >>> d.spam
    'eggs'
    >>> d.spam = 100
    >>> d['spam']
    100


``DotDictMixin``
================

A mixin class to provide attribute access to dict-like classes. Both ``DotDict`` and ``DotDictMixin`` are implemented using this mixin like this::

    class DotDict(DotDictMixin, dict): pass
    
