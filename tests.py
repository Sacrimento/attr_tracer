from attr_debug import Attr_debug

@Attr_debug('X')
class A():
    X = 5

a = A()
a.X = 6
print(a.X)