class Myclass:
    def __init__(self, name):
        self.name = name
    #重写方法，使得直接打印该类的结果变化
    def __str__(self):
        print('print call __str__')
        return 'hello' + self.name;
    #重写迭代器方法，同时重写__init__,__str__,__next__（真正做计算的函数）
    def  __iter__(self):
        return self
    def __next__(self):
        pass

    def myPrint(self):
        print(__name__)


print(__name__)
print(Myclass('Tom'))