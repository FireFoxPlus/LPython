#重写call
class Myclass:
    def __call__(self):
        print("call cls")

cls = Myclass()
print(callable(cls))
cls()