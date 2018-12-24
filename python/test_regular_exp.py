#!/usr/bin/python
import re
line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group():",matchObj.group())
else:
    print("match --> matchObj.group():No match!!")

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print("search --> matchObj.group():", matchObj.group())
else:
    print("search --> matchObj.group():No match!!")

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print("matchObj.group() :",matchObj.group())
    print("matchObj.group(1) :",matchObj.group(1))
    print("matchObj.group(2) :",matchObj.group(2))
else:
    print('No match!!')

s = '1102231990xxxxxxxx'
ret = re.search('(?P<群组1>\d{3})(?P<群组2>\d{3})(?P<群组3>\d{3})',s)
print(ret.group())
print(ret.group(1))
print(ret.group(2))
print(ret.group(3))
print(ret.groupdict())
a=re.match(r'(tina)(fei)(ha)\3','tinafeihahafei tinafeihahatina').group()
print(a)

w = re.findall('\btina','tian tinaaaa')
print(w)
s = re.findall(r'\btina','tian tinaaaa')
print(s)
v = re.findall(r'\btina','tian#tinaaaa')
print(v)
a = re.findall(r'\btina\b','tian#tina@aaa')
print(a)

pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)