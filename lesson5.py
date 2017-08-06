#简单的文件直接读写
file1 = open("test.txt")
file2 = open("output.txt","w")
while True:
   line = file1.readline()
   file2.write(line)
   if not line:
       break

file1.close()
file2.close()

#文件迭代器
file2 = open("output2.txt","w")
for line in open("test.txt"):
    file2.write(line)

#文件上下文迭代器,自带文件关闭功能
#读
with open('test.txt','r') as f:
    data = f.read()
    print(data)
#写
with open('output3.txt', 'w') as f:
    f.write('only test message')
#用printf进行写入文件
with open('output4.txt','w') as f:
    print('another test', file=f)

#二进制文件读写
f = open('test.txt', 'rb')
print(f.read())
#解码,参数为解码方式
u=f.read().decode('utf-8')

#文件和目录操作
import os
print(os.name)
#print(os.uname())
#查看环境变量,list
print(os.environ)
#当前绝对路径
print(os.path.abspath('.'))

#在某个目录下创建一个新目录
#1.得到表示新路径,用这个函数而不是字符串加法，可以保证\分隔符的正确
path = os.path.join(os.path.abspath('.'),'pics')
#os.mkdir(path)
#删除文件夹
#os.rmdir(path)

#拆分一个路径因为分割符，也要用如下函数
#将最右与其他部分分离
print(os.path.split('/USER/EDC/Pics/Mem.jpg'))

#获得扩展名
print(os.path.splitext('/USER/EDC/Pics/Mem.jpg'))

#文件重命名
#os.rename('output.txt','rename.txt')
#删除文件
#os.remove('rename.txt')
#没有复制文件的api函数，可以引入第三方库
import shutil
shutil.copyfile('./test.txt','./zhang.txt')

#列出当前目录下为所有目录
dir = [x for x in os.listdir('.') if os.path.isdir(x)]
for x in dir:
    print(x)

#只列出py文件
py = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
for x in py:
    print(x)

#序列化和反序列化
import pickle
#定义一个dict字典对象
d = dict(name = 'zz', age=29, score=80)
str = pickle.dumps(d)
print(str)
#写入文件
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

#反序列化
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

#用json实现序列化和反序列化
import json
d1 = dict(name = 'tt', age='20')
str = json.dumps(d1)
print(str)
#反序列化
d2 = json.loads(str)
print(d2)

#高阶函数
def add(x , y , f):
    return f(x) + f(y)
print(add(4, -5, abs))

#匿名函数
#lambda创建匿名函数
sum  = lambda arg1, arg2: arg1 + arg2
print(sum(10, 30))
#reduce
from functools import reduce
l = [1,2,3,4,5]
print(reduce(lambda x,y : x + y, l))
#第三个参数为x初始值
print(reduce(lambda x,y : x + y, l, 10))
#map
l1 = [1,2,3]
l2 = [2,3,4]
new_list = list(map(lambda i: i + 1, l))
print(new_list)
new_list2 = list(map(lambda x,y : x + y, l1, l2))
print(new_list2)
#filter
l = [100,20,24,50,110]
new = list(filter(lambda x : x < 50 , l))
print(new)

#装饰器，也可以用类做装饰器
from functools import wraps
def hello(fn):
    #使用wrap装饰，可以消除装饰器的副作用，__name__仍然是foo，而不是wrapper
    @wraps(fn)
    def wrapper():
        print('hello ' + fn.__name__)
        fn()
        print('bye ' + fn.__name__)
    return wrapper
@hello
def foo():
    print('i am foo')
foo()

#斐波拉切数列
def memo(fn) :
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        #返回查找到的值，否则返回miss
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result
    return wrapper

@memo
def fib(n):
    if n < 2:
        return n
    return fib( n -1 ) + fib(n - 2)

print(fib(6))

#偏函数
import  functools
int2 = functools.partial(int , base = 2)
print(int2('10010'))
#作为dict带入
kw = {'base':2}
print(int('10010', **kw))
#塞入list
max2=functools.partial(max, 10)
print(max2(5,6,7))



