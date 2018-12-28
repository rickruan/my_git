# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__='Rick Ruan'
import xlrd

book = xlrd.open_workbook('Ruan_excel_1.xls')
sheet = book.sheet_by_index(0)
sheet2 = book.sheet_by_name('测试表格1')
print(sheet.cell(0, 0).value)
print(sheet.cell(0, 1).value)
print(sheet.cell(0, 2).value)
print(sheet.cell(0, 3).value)

print(sheet.ncols)
print(sheet.nrows)
print(sheet2.ncols)
print(sheet2.nrows)

print(sheet.get_rows())
for i in sheet.get_rows():
    print(i)

print(sheet.row_values(0))
for i in range(sheet.nrows):
    print(sheet.row_values(i))

print(sheet.col_values(0))
for i in range(sheet.ncols):
    print(sheet.col_values(i))

for i in range(sheet2.nrows):
    print(sheet2.row_values(i))