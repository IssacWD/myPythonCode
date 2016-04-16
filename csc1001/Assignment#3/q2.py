# coding=utf-8
# ********************************************************
#   > OS     : OS X 10.11.3
# 	> Author : JasonGUTU
# 	> Mail   : intergujinjin@foxmail.com
# 	> Time   : 2016/4/16
# ********************************************************
# The Question Two

class InputError(BaseException):
    def __init__(self, message=None):
        if message is not None:
            print(message)
        else:
            print('Please check your polynomial.')


class Polynomial:

    def __init__(self, polynomial_str):
        self.polynomial = polynomial_str
        self.__list_poly_terms = list()
        self.__list_poly_derivative_terms = list()
        self.variable = str()
        self._parser_polynomial()

    def _parser_polynomial(self):
        replaced_str = self.polynomial.replace('-', '+-')
        self.__list_poly_terms = replaced_str.split('+')

    def _derivative_variable(self, term):
        term_list = term.split('^')
        if len(term_list) == 1:
            term = '1'
            return 1, '1'
        variable = str()
        coefficient = 1.0
        for item in term_list:
            if item.isalpha():
                if self.variable is None:
                    self.variable = item
                    continue
                if self.variable != item:
                    raise InputError()
                variable = item
            else:
                try:
                    coefficient = eval(item)
                except:
                    raise InputError()
        return str(coefficient), variable + '^' + str(coefficient - 1)

    def _derivative_every_term(self, term):
        import re
        numbers = re.compile(r'[0-9\.\-]')
        result_term = str()
        if '*' not in term:
            if numbers.match(term):
                result_term = '0'
            else:
                coefficient, var_part = self._derivative_variable(term)
                result_term = coefficient + '*' + var_part
        else:



    def getDerivative(self):
        for item in self.__list_poly_terms:

