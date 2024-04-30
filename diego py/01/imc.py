import os

nome = input("Digite seu nome: ")

os.system('clear')

peso = float(input("Digite seu peso: "))

os.system('clear')

altura = float(input("Digite sua altura: "))

os.system('clear')

resultado = peso / (altura*altura)


if resultado < 18.5:
    print(f"Sr(a) {nome}, seu IMC é: {resultado:.1f}, sua situação é abaixo do peso!")
elif resultado >= 18.5 and  resultado < 25:
    print(f"Sr(a) {nome}, seu IMC é: {resultado:.1f}, sua situação é peso ideal!")
elif resultado >= 25 and resultado < 29.9:
   print(f"Sr(a) {nome}, seu IMC é: {resultado:.1f}, sua situação é levemente acima do peso!")     
elif resultado >= 30.0 and resultado <= 34.9:
    print(f"Sr(a) {nome}, seu IMC é: {resultado:.1f}, sua situação é obesidade grau 1!")
elif resultado >= 35.0 and resultado <= 39.9: 
    print(f"Sr(a) {nome}, seu IMC é: {resultado:.1f}, sua situação é obesidade grau 2(severo)!")
elif resultado >= 40:
    print(f"Sr(a) {nome}, seu IMC é: {resultado:.1f}, sua situação é obesidade grau 3(mórbida)!")