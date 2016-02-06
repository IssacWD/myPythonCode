# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/5
#********************************************************
# The Question One
final_account = eval(input("Enter the final account value:"))
interest_rate = eval(input("Enter the annual interest rate:"))
years = eval(input("Enter the number of years:"))
print("The initial value is ", final_account / (1 + interest_rate * 0.01) ** years)

