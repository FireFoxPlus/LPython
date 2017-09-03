import re

#正则表达式
#加上r之后，\不用再转义了
m = re.match(r'dog', 'dog cat dog')
print(m.group())
print(re.match(r'cat', 'dog cat dog'))
s = re.search(r'cat', 'dog cat dog')
print(s.group())
print(re.findall(r'dog', 'dog cat dog'))

contactinfo = 'Doe,John:555-1212'
m = re.search(r'(\w+),(\w+):(\S+)', contactinfo)
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.group(0))