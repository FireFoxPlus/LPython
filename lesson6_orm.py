#列名和该列的数据类型
class Filed:
    def __init__(self,name,col_type):
        self.name = name
        self.col_type = col_type

class IntegerField(Filed):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'integer')


class StringFiled(Filed):
    def __init__(self, name):
       super(StringFiled, self).__init__(name, 'varchar(1024)')

class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Model name',name)
        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, Filed):
                print('Filed name ', k)
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kvs):
        super(Model, self).__init__(**kvs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError('Model has no attribute', item)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k , None))

class user(Model):
    id = IntegerField('id')
    name = StringFiled('name')

#u = user(id= 100,name='Tom')
u = user()
u.id=100
u.name='test'
u.save()
print(u)