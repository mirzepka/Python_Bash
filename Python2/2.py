import os
import math

class Complex:

    def __init__(self, re, im):
        self.re=re
        self.im=im

    def __str__(self):
        return "Imag={} , Real={}".format(self.im,self.re)

    def __add__(self, other):
        return Complex(self.re+other.re,self.im+other.im)

    def __sub__(self, other):
        return Complex(self.re-other.re,self.im-other.im)

    def __mul__(self, other):
        return Complex(self.re*other.re-self.im*other.im,self.re*other.im+self.im*other.re)

    def modulo(self):
        return math.sqrt(self.re*self.re+self.im*self.im)

