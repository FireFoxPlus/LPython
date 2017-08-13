#实现下标访问
class Fib:
    def __getitem__(self, item):
        a, b = 1, 1
        for i in range(item):
            a, b = b, a + b
        return a


f = Fib()
print(f[5])
