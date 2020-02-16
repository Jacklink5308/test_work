#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from selenium import webdriver
from pprint import pprint
import time

#创建浏览器对象
driver = webdriver.Chrome()
#控制浏览器访问 https://www.51job.com
driver.get('https://www.51job.com')
#隐式等待 6s
driver.implicitly_wait(6)
#找到关键字输入框并输入 需查询岗位（测试）
keyWord = driver.find_element_by_id('kwdselectid')
keyWord.send_keys('测试')
#选择岗位所在城市
position = driver.find_element_by_id('work_position_input')
position.click()
#使用css选择器将已点亮城市选择后点灭
time.sleep(1)
eles = driver.find_elements_by_css_selector('#work_position_click_center_right em[class=on]')
for ele in eles:
    ele.click()

#选择需选择城市（杭州）
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()
#选择完成点击确定按钮
driver.find_element_by_id('work_position_click_bottom_save').click()
time.sleep(1)
#点击搜索
driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/button').click()

#搜索结果分析

import xlwt
#创建一个Excel  workbook 对象
book1 = xlwt.Workbook()
#增加一个子表sheet
sheet1= book1.add_sheet('杭州-测试岗位表')

#标题分析
job_title = driver.find_element_by_css_selector("#resultList div[ class='el title' ]")
job_title_texts = job_title.find_elements_by_tag_name('span')
title_string = [job_title_text.text for job_title_text in job_title_texts ]
# pprint(' | '.join(title_string))
#将标题写入sheet1
col_1 = 0
for job_title_text in job_title_texts:
    sheet1.write(0,col_1,job_title_text.text)
    col_1 += 1

#工作内容分析
jobs = driver.find_elements_by_css_selector('#resultList div[ class=el ]')
row = 1
for job in jobs:
    fields = job.find_elements_by_tag_name('span')
    string_job = [field.text for field in fields]
    # pprint(' | '.join(string_job))
    col = 0
    for field in fields:
        text = field.text
        #将每一条工作信息写入excel表
        sheet1.write(row,col,text)
        col += 1
    row += 1

#保存EXCEL文件
book1.save(r'F:\1_work\test_work\jobs.xls')
#关闭浏览器对象
driver.quit()

