# !/usr/bin/python3
# coding=utf-8
# ********************************************************
#   > OS     : OS X 10.11.3
#   > Author : JasonGUTU
#   > Mail   : hellojasongu@gmail.com
#   > Time   : 2016/4/28
# ********************************************************
import openpyxl
import pickle


def str_method(code):
    if code == 200:
        return 'OK'
    elif code == 400:
        return 'Wrong request'
    elif code == 403:
        return 'Prohibit access'
    elif code == 404:
        return '404 Not Found'
    else:
        return 'Something Wrong'


if __name__ == '__main__':
    result = open('re.plk', 'rb')
    result_list = pickle.load(result)
    workbook = openpyxl.load_workbook('URL.xlsx')
    sheet = workbook.get_sheet_by_name(workbook.get_sheet_names()[0])
    for url_package in result_list:
        index = url_package[0] + 1
        cell_number = 'H' + str(index)
        sheet.cell(cell_number).value = str_method(url_package[1])
    workbook.save(filename='new.xlsx')
