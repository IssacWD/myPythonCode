# coding=utf-8
#********************************************************
#   > OS     : Ubuntu 15.10
#	> Author : JasonGUTU
#	> Mail   : intergujinjin@foxmail.com
#	> Time   : 2016/3/30
#********************************************************
# The Question One

class Flower:
    def __init__(self):
        self.name = 'init name'
        self.number_of_petals = 5
        self.price = 1.0

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getNumberOfPetals(self):
        return self.number_of_petals

    def setName(self, name):
        if not isinstance(name, str):
            pass
        else:
            self.name = name

    def setPrice(self, price):
        if not isinstance(price, float) or not isinstance(price, int):
            pass
        else:
            self.price = price

    def setNumberOfPetals(self, number_of_petals):
        if not isinstance(number_of_petals, int):
            pass
        else:
            self.number_of_petals = number_of_petals

if __name__ == '__main__':
    print('Flower class.')