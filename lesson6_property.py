import  traceback

class Student:
    @property
    def score(self):
        return self._score

    #如果注释掉次此方法，相当于实现了一个只读属性
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise  ValueError('not int')
        elif(value < 0) or (value > 100):
            raise ValueError('not valid')
        else:
            self._score = value

s = Student()
s.score = 75
print(s.score)