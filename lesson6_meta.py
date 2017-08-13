#额外增加add方法，实际等价于append
def add(self, value):
    self.append(value)

class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):
        print(cls)
        print(name)
        print(bases)
        print(type(attrs),attrs)
        #attrs['add'] = lambda self,value:self.append(value)
        attrs['add'] = add
        attrs['name'] = 'Tom'
        return type.__new__(cls, name, bases, attrs)


class Mylist(list, metaclass=ListMetaClass):
    pass

mli = Mylist()
mli.add(1)
mli.add(2)
mli.add(3)
print(mli)