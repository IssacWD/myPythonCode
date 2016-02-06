# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/5
#********************************************************
# The Question Four
def get_number_and_judge():
    number = input("Enter an integer:")
    if not number.isdigit():
        print("Wrong input")
        number = get_number_and_judge()
    if eval(number) < 0:
        print("Wrong input")
        number = get_number_and_judge()
    return int(number)


def display(number):
    print("m      m+1    m**(m+1)")
    for i in range(number):
        print(format(i + 1, '<6d'), format(i + 2, '<6d'), (i + 1) ** (i + 2))


display(get_number_and_judge())
