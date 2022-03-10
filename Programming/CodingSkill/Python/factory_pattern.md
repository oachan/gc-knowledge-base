# Factory Pattern

## 使用 __metaclass__ 寫 factory pattern 的方法.
``` python
class ShapeFactory(type):

    def __call__(cls, desc):
        if cls is Shape:
            if desc == 'big':   return Rectangle(desc)
            if desc == 'small': return Triangle(desc)
        return type.__call__(cls, desc)


class Shape(object):

    __metaclass__ = ShapeFactory 

    def __init__(self, desc):
        print "init called"
        self.desc = desc


class Triangle(Shape):
    
    def __init__(self, desc):
        super(Triangle, self).__init__(desc)

    @property
    def number_of_edges(self): return 3


class Rectangle(Shape):
    
    def __init__(self, desc):
        super(Rectangle, self).__init__(desc)

    @property
    def number_of_edges(self): return 4


print Shape('big').number_of_edges
print Shape('small').number_of_edges
```

## Ref
- https://stackoverflow.com/questions/5953759/using-a-class-new-method-as-a-factory-init-gets-called-twice