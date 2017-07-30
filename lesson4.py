class student:
    #类属性
    grade = 91
    #一般函数
    def bar(self, name):
        print("self.name=" + self.__name)
        print("function`s varible name=" + name)
    #构造函数
    def __init__(self ,name):
        #有别于self.name，如下写法相当于是私有变量(即2个下划线开头，私有方法也以此命名)，不可通过.的方式进行更改
        self.__name = name
        self.age = 19
    #对于私有变量的get、set方法
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

#继承于student
class primaryStudent(student):
    def lol(self):
        print('play lol')

obj1 = student('Anna')
obj1.bar('not self.name')

obj2 = primaryStudent('Sum')
obj2.bar('sum')

#返回所有可用的属性和方法
print(dir(obj2))
print(type(dir(obj2)))

#测试对象是否含有属性
print(hasattr(obj1, 'age'))
print(hasattr(obj1, 'bar'))
#得到函数并得到指向其的变量
fn = getattr(obj1, 'bar')

#当前python目录
import sys
print(sys.path)




