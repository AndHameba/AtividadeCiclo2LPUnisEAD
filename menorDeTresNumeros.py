# -*- coding: latin1 -*-

a1 = int(input('Digite o primeiro numero: '))
b2 = int(input('Digite o segundo numero: '))
c3 = int(input('Digite o terceiro numero: '))

if (a1 < b2) and (a1 < c3):
    print ('O menor numero e o primeiro: %d' % a1)
elif (b2 < a1) and (b2 < c3):
    print ('O menor numero e o segundo: %d' % b2)
elif (c3 < a1) and (c3 < b2):
    print ('O menor numero e o terceiro: %d' % c3)
else:
    print ('O numero que voce digitou esta incorreto ou repetido!!!')