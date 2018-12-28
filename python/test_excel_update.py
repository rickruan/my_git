# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__='Rick Ruan'

from xlutils.copy import copy
import xlrd

book = xlrd.open_workbook('Ruan_excel_1.xls')
book1 = copy(book)
print(dir(book))

sheet = book1.get_sheet(0)
sheet.write(1,3,'100')
sheet.write(1,0,'Grace')

book1.save('Ruan_excel_1.xls')