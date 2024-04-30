import os

nome = input('Digite seu nome: ')

os.system("clear")

valor01 = float(input('Digite o primeiro numero: '))

os.system("clear")

valor02 = float(input('Digite o segundo numero: '))

os.system("clear")

resultado = valor01 * valor02

print(f'Sr(a) {nome}, o resultado da multiplicação feita foi: {resultado:.0f}')