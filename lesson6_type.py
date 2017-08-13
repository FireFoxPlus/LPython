def init(self,name):
    self.name = name
def say_hello(self):
    print('hello',self.name)
#用type创建类
Hello = type('Hello', (object, ), dict(__init__=init, hello = say_hello))
#Hello = type('Hello', (object, ), {'__init__':init, 'hello':say_hello})
print(type(Hello))
h = Hello('Tom')
h.hello()
