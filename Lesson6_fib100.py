#迭代器实现示例，所有的计算都是在__next__中实现的
class Fib100:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.first,self.second = self.second,self.first + self.second
        if self.first > 100:
            raise StopIteration()
        return self.first

for i in Fib100():
    print(i)