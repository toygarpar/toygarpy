class AttrDisplay:

    """
    Provides an inheritable display overload method that shows
    instances with their class names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """


    def attrToparla(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append("{} = {}".format(key, getattr(self, key)))

        return ", ".join(attrs)


    def __repr__(self):
        return "[{}: {}]".format(self.__class__.__name__, self.attrToparla())


if __name__ == "__main__" :

    class Test(AttrDisplay):
        count = 0 
        def __init__(self):
            self.attr1 = Test.count
            self.attr2 = Test.count + 1
            Test.count += 2

    class Subtest(Test):
        pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
class E: pass
class F(D, E): pass 
    
F.__bases__


D.__bases__
