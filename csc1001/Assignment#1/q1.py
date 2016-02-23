# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 14.04
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/2/5
#********************************************************
# The Question One
from AssTools.getInput import get_number

if __name__ == '__main__':
    final_account = get_number('Enter the final account value:', sign=1, int_type=False)
    interest_rate = get_number('Enter the annual interest rate:', sign=1, int_type=False)
    years = get_number('Enter the number of years:', sign=1)
    print("The initial value is %s yuan" % format(final_account / (1 + interest_rate * 0.01) ** years, '.2f'))

