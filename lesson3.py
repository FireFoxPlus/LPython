#list
l1 = [1,2,3,'46',[1,2,3],{1:'one',2:'two'}]
print(type(list))
print(type(l1))
print(l1[0])
#从末尾索引
print(l1[-1])

#查找元素位置
print(l1.index('46'))
print(l1.index([1,2,3]))

#添加元素
l2=[1, 2, 3]
l2.append(4)
#数组整体添加
l2.extend([5, 6, 7])
print(l2)
#删除元素
del(l2[-1])
l2.remove(1)
print(l2)
#判断容器是否为空,空和None并不等价
l3=[]
if not l3:
     print('empty')
if l3 is None:
    print('none')
if len(l3) == 0:
    print('empty')

#元组
t=(1, 2, 3)
#只读，复制报错
#t[0]='a'

#字典
d={'a':1, 'b':2, 3 :[1,2,3]}
print(type(d))
print(type(dict))
print(d)
#访问元素
print(d['a'])
print(d[3])
#判断key是否而存在
print('a' in d)
#删除元素,下标是key的值
del(d[3])
#根据key遍历
for key in d :
    print(d[key])
#根据key，value遍历
for key, value in d.items():
    print(key, value)
#拿出所有的key
keys = d.keys();
print(type(keys))
print(keys)
#添加元素,若key存在则会覆盖value
d['c']='345'

#set 去重
s1=set([1,2,2,3,4,5])
s2=set([1,2,3,6,7,8])
print(s1)
#判断元素是否存在
print(1 in s1)
#并集
print(s1 | s2)
print(s1.union(s2))
#交集
print(s1 & s2)
print(s1.intersection(s2))
#差集
print(s1 - s2)
print(s1.difference(s2))
#对称差
print(s1 ^ s2)
print(s1.symmetric_difference(s2))
#添加元素
s1.add(2)
#数组整体添加
s1.update([10,11])
#删除元素，直接指定值
s1.remove(1)

#切片
li = list(range(10))
print(li)
#[start:end:steps]
print(li[2:5])
print(li[:4])
print(li[5:])
print(li[0:10:3])
#负值处理和运用
print(li[5:-2])
print(li[9:0:-1])
#快速反转
print(li[::-1])

#列表推导
li = [0] * 10
#前10个偶数
li= [i * 2 for i in range(10)]
print(li)
#二维数组
#相当于将一行复制了3次，但是是浅拷贝
li= [[0] * 3] * 3
li[0][0]=100
print(li)
#真正的生成独立的三行，深拷贝
li=[[0] * 3 for i in range(3)]
li[0][0]=100
print(li)
#list
li={i for i in range(10) if i%2==0}
print(li)
#dict
li={x : x%2==0 for x in range(10)}
print(li)

#生成器
#平方表
square = (x * x for x in range(10000))
for i in range(10):
    print(next(square))

#迭代器
from collections import Iterable
from collections import  Iterator
#判断是否可迭代
print(isinstance([1,2,3], Iterable))
print(isinstance('123',Iterable))
print(isinstance({}, Iterable))





