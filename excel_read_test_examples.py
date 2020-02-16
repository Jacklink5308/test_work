#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import xlrd
from pprint import pprint
import json
#读取excel测试用例
excelDir = r'F:\1_work\test_work\test1.xls'
#打开excel
workbook = xlrd.open_workbook(excelDir)
#查看excel全部子表
pprint(workbook.sheet_names())
#选择子表
worksheet = workbook.sheet_by_name('接口为文档')
#读1行
rows = worksheet.row_values(0)
pprint('子表-接口文档内容：')
pprint(rows)
#读1列
clos = worksheet.col_values(1)
pprint(clos)
#读某单元格
cellData = worksheet.cell_value(1,1)
pprint(cellData)

#读子表-新建客户1
worksheet2 = workbook.sheet_by_name('新建客户1')

#读子表2的第二行
sheet_row2 = worksheet2.row_values(1)
pprint('子表2的第二行：')
pprint(sheet_row2)
cellData = worksheet2.cell(1,1).value
cellData_ = worksheet2.cell_value(1,1)
cellType = worksheet2.cell(1,1).ctype
pprint(cellData)
pprint(cellData_)
pprint(cellType)


#将测试结果写入excel
#import xlutils
from xlutils.copy import copy
#打开excel
# workbookWr = xlrd.open_workbook(11)
#复制
excel_res = 'pass;测试通过'
workbookWr = copy(workbook)
wrSheet = workbookWr.get_sheet(1)
wrSheet.write(1,3,excel_res)
excelDir_save = r'F:\1_work\test_work\test1_1.xls'
workbookWr.save(excelDir_save)



a = []
print(type(a))