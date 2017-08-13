import traceback
from types import MethodType

class Myclass(object):
    #限定能添加的属性名或方法名
    __slots__ = ['name','set_name']
def set_name(self, name):
    self.name=name
cls = Myclass()
cls.name='Tom'
#为实例添加方法
cls.set_name = MethodType(set_name, cls)
cls.set_name('Jerry')
print(cls.name)
#为实例添加属性
try:
    cls.age=30
except AttributeError:
    traceback.print_exc()

class ExtMyClass(Myclass):
    pass
ext_cls = ExtMyClass()
ext_cls.age = 30
print(ext_cls.age)