# -*- coding: latin1 -*-

def inversao(pal):

    aveso = pal.split()
    for i in xrange(len(aveso)):
        aveso[i] = aveso[i][::-1]
    return ' '.join(aveso)

pal = 'Sistemas de Informacao Unis MG'
print inversao(pal)
