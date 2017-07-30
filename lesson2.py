import string

# 去除空格
s  =  '    asdjkjl   ajsdljl   '
#删除左右空格
print(s.strip())
#删除左空格
print(s.lstrip())
#删除右空格
print(s.rstrip())

#连接字符串
s1 = 'abc'
s2 = 'def'
print(s1 + s2)

#大小写转换
s = 'abc def'
#全大写
print(s.upper())
#全小写
print(s.upper().lower())
#首字母大写
print(s.capitalize())

#字符串查找
s1 = 'abcdef'
s2 = 'bcd'
print(s1.index(s2))

#字符串比较
print(s1 == s2)
print(s1 > s2)
print(s1 < s2)

#字符串长度
print(len('abcde'))

#字符串分割
s = 'abc,def,ghi'
splitted = s.split(',')
print(type(splitted))
print(splitted)
#按行分割
s = """abc
def
ghi"""
print(s.split('\n'))
print(s.splitlines())

#字符串连接
s = ['abc', 'def','ghi']
print('-'.join(s))

#常用判断
s =  'abcdef'
print(s.startswith('abf'))
print(s.endswith('def'))
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.isspace())
print(s.islower())
print(s.istitle())

#数字到字符串的转换
print(str(5))
print(int('22345'))
print(float('23.45'))
#进制转换
print(int('110111',  2))

#字符串转换为数组
s = 'abcdefg'
l = list(s)
print(l)

#for循环
for i in range(0, 30, 5):
  print(i)

#while循环
s = 0
i = 1
while i<= 100:
  s += i
  i  += 1
print(s)

#函数,返回多个值
def func_name(arg1, arg2):
    print(arg1)
    print(arg2)
    return arg1, arg2

r = func_name(1, 2)
print(type(r))
print(r[0], r[1])

#匿名可变参数,tuple
def  func(name , *numbers):
   print(type(numbers))
   print(numbers[1])

func('tom',1,2,3,4)

#命名可变参数 means
def func(name, **kvs):
    print(name)
    print(type(kvs))
    print(kvs)

func('Tom', china='Beijing' , uk='London')

#命名变量
def  func(a,b,c,*,china,uk):
  print(china, uk)

func(1,2,3,china='BJ',uk='LD')

#复杂情况
def func(a, b, c=0, *args, **kvs):
    print(a, b, c)
    print(args)
    print(kvs)

func(1, 2)
func(1, 2, 3)
func(1, 2, 3, 'a', 'b', 'c' )
func(1, 2, 3, 'a', 'b', 'c', china='BJ', uk='LD')
#更清晰的调用方式
func(1, 2, 3, *('a', 'b', 'c'),  **{'china' : 'BJ', 'uk' : 'LD'})

#函数做参数
p=print
p(1,2,3)

def sum(x, y ,p = None):
    s = x + y
    if p:
        p(s)
    return s
sum(100, 200)
sum(100, 200, print)



     













