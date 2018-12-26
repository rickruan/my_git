#!/usr/bin/python
# -*- coding: UTF-8 -*-
#  定义函数


def t_func(var):
    try:
        return int(var)
    except ValueError as e:
        print("参数没有包含数字\n", e)


try:
    fh = open("ruan_test", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()

try:
    fh = open("ruan_test", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print("关闭文件")
        fh.close()

except IOError:
    print("Error: 没有找到文件或读取文件失败")

# 调用函数
t_func('xyz')


def mye(level):
    if level < 1:
        raise Exception('Invalid level:%s',level)


try:
    mye(0)
except Exception as e:
    print(e)
else:
    print("End!")
