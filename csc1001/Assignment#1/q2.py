# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/5
#********************************************************
# The Question Two
str_number = input("Enter an integer:")
if str_number.isdigit():
    for char in str_number:
        print(char)
else:
    print("wrong input")