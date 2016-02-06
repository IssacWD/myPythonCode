# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/5
#********************************************************
# The Question Five
def get_number_and_judge():
    number = input("Enter an integer:")
    if not number.isdigit():
        print("Wrong input")
        number = get_number_and_judge()
    if eval(number) < 2:
        print("Don't have any number.")
        number = get_number_and_judge()
    return int(number)


