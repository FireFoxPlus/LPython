#一个类实现了__set__/__get__/__del__方法的类称为描述器

class MyProperty:
    def __init__(self, fget= None, fset=None, fdel = None):
        print(fget)
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        if self.fget:
            print('__fget')
            return self.fget(instance)
    def __set__(self, instance, value):
        if self.fset:
            print('__get')
            return self.fset(instance, value)
    def __delete__(self, instance):
        if self.fdel:
            return  self.fdel(instance)
    def getter(self,fn):
        self.fget = fn
    def setter(self, fn):
        print('setter', fn)
        self.fset = fn
    def deler(self,fn):
        self.fdel = fn

class student:
    @MyProperty
    def score(self):
        return self._score

    @score.setter
    def set_score(self, value):
        self._score = value

s = student()
s.score = 95
print(s.score)