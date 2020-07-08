## TODO
# Use an existing logger ?
# Be able to handle more than one attribute ?
# Hide this class (type ?)

import inspect
import sys

class Attr_debug:
    _attr = None

    def __init__(self, attr_name):
        self.attr_name = attr_name

    def __call__(self, cls):
        def wrapper(*args, **kwargs):
            super(Attr_debug, self).__init__(*args, **kwargs)
            attr = property(fset=self._attr_setter, fget=self._attr_getter)
            setattr(self, self.attr_name, attr)
            self._attr = getattr(self, self.attr_name)
            return self
        return wrapper

    def __getattribute__(self, attr):
        obj = object.__getattribute__(self, attr)
        if isinstance(obj, property):
            return obj.fget()
        return super(Attr_debug, self).__getattribute__(attr)

    def __setattr__(self, attr, val):
        obj = getattr(self, attr, None)
        if isinstance(obj, property):
            return obj.fset(val)
        return super(Attr_debug, self).__setattr__(attr, val)

    def _attr_getter(self):
        return self._attr

    def _attr_setter(self, val):
        
        print(sys._getframe(1))

        self._attr = val
