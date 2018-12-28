# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__='Rick Ruan'
import xlwt
stus = [['姓名','年龄','性别','分数'],
    ['Mary',20,'女',90],
    ['Gracy',40,'女',90.5],
    ['Jodan',25,'男',98],
    ['MaryLy',20,'女',100]
    ]

book = xlwt.Workbook()
sheet = book.add_sheet('测试表格1')
row = 0
for stu in stus:
    col = 0
    for s in stu:
        sheet.write(row,col,s)
        col += 1
    row += 1
book.save('Ruan_excel_1.xls')