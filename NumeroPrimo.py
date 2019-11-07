# -*- coding: latin1 -*-

def is_prime(alg):
    if alg < 2:
        return 'Nao e Primo'
    for i in range(int(2), alg):
        if not alg % i:
            return 'Nao e Primo'
    else:
        return 'E Primo'

for j in range(1,101):
    print j, is_prime(j)

