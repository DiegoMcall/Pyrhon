import os

nome = input('Digite seu nome: ')

os.system('clear')

uni1 = float(input('Digite sua 1ª nota: '))

os.system('clear')

uni2 = float(input('Digite sua 2ª nota: '))

os.system('clear')

uni3 = float(input('Digite sua 3ª nota: '))

os.system('clear')

media = (uni1+uni2+uni3)/3

if media >= 7:
    print(f'{nome} sua média foi: {media}, você foi aprovado!')
elif media >= 5 and media < 7:
    print(f'{nome} sua média foi: {media}, você foi para a prova final!')
else:
    print(f'{nome} sua média foi: {media}, você foi para recuperação!')    
