nome1 = ['me', 'mu', 'ma', 'gi', 'cla', 'ju', 'an', 'mu', 'a']
nome2 = ['a', 'li', 'la', 'ra', 'dio', 'deu', 'ria', 'ria']
nome3 = ['ana', 'nei', 'tam', 'io', 'dith', 'tos', 'na', 'pu', 'te']

juncao1 = nome1+nome2
juncao2 = nome2+nome3
juncao3 = nome3+nome1

import random


def nomeCompleto():
    nome = random.choice(juncao1)
    nomeMeio = random.choice(juncao2)
    nomeFinal = random.choice(juncao3)

    return nome+nomeMeio+nomeFinal

contador1 = 24
numero = 0

while contador1 !=0:
    numero = numero+1
    print(numero, nomeCompleto().title(), nomeCompleto().title())
    contador1 = contador1-1
print("Primeiro time pronto!")
print("\n")

contador2 = 24
numero = 0

while contador2 !=0:
    numero = numero+1
    print(numero, nomeCompleto().title(), nomeCompleto().title())
    contador2 = contador2-1
print("Segundo time pronto!")
    
