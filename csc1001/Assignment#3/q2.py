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
    """ Class for polynomial """
    def __init__(self, polynomial_str):
        self.polynomial = polynomial_str
        self.__list_poly_terms = list()
        self.__list_poly_derivative_terms = list()
        self.variable = None
        for letter in polynomial_str:
            if letter.isalpha():
                if self.variable is not None and letter != self.variable:
                    raise InputError
                else:
                    self.variable = letter
        self._parser_polynomial()

    def _parser_polynomial(self):
        replaced_str = self.polynomial.replace('-', '+-')
        self.__list_poly_terms = replaced_str.split('+')

    def _parser_power(self, term):
        term_list = term.split('^')
        if len(term_list) == 1:
            return 0, ''
        for part in term_list:
            if self.variable in part:
                continue
            coefficient = int(part)
        return coefficient, self.variable + '^' + str(coefficient - 1)

    def _derivative_term(self, term):
        negative = False
        if term.startswith('-'):
            negative = True
            term.replace('-', '')
        term_list = term.split('*')
        if len(term_list) == 1:
            if self.variable in term_list[0]:
                coefficient, var_str = self._parser_power(term_list[0])
                result_str = str(coefficient) + '*' + var_str
            else:
                result_str = ''
        else:
            for part in term_list:
                if self.variable in part:
                    coefficient, var_str = self._parser_power(part)
                else:
                    mul = eval(part)
            result_str = str(coefficient * mul) + '*' + var_str
        if negative:
            result_str = '-' + result_str
        else:
            result_str = '+' + result_str
        return result_str

    def getDerivative(self):
        derivative_str_list = list()
        for item in self.__list_poly_terms:
            derivative_str_list.append(self._derivative_term(item))
        return ''.join(derivative_str_list)[1:]


if __name__ == '__main__':
    test_a = '2*x^3+4*x^4+4+x^2+x'
    a = Polynomial(test_a)
    print(a.getDerivative())
