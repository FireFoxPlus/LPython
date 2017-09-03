from functools import reduce
def inc(x):
    def incx(y):
        return  x + y
    return incx

inc2 = inc(2)
inc5 = inc(5)

print(inc2(5))
print(inc5(5))
#lamda函数
g = lambda x : x * 2
print(g(3))
print((lambda x : x * 2)(4))

#计算数组中正数的平均数
num = range(-5,5)
positive_num = list(filter(lambda x : x > 0, num))
average = reduce(lambda x, y : x + y, positive_num)/len(positive_num)