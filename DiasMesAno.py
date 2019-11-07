#-*- coding: latin1 -*-

barra = '======================================================='

print barra

nvida = int(input('Insira o numero de dias de vida: '))

ano = int(nvida / 365)

print ('%d anos ' % ano)

print barra

m = int((nvida / 30)) - (ano * 12)

print ('%d meses ' % m)

print barra

if nvida == 365:
    d = 0
else:
    d = nvida - ((nvida / 30) * 30)
    print ('%d dias ' % d)

print barra