# -*- coding: latin1 -*-
barra = '========================================================'
a = int(input('Declare um valor para A: '))
b = int(input('Declare um valor para B: '))
c = int(input('Declare um valor para C: '))

import math

if a > (b + c):
    print 'Se A e o lado maior nao pode ser um triangulo!'
    print barra
else:
    j = (a + b + c) / 2
    l = j * (j - a) * (j - b) * (j - c)
    h = math.sqrt(l)
    print 'Este triangulo tem uma area de: ', h
    print barra
