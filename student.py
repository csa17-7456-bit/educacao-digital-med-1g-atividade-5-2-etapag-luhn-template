Nome: Luiza Ulhoacartao = input().strip()
digitos = [int(x) for x in cartao]
digitos.reverse()

soma_impares = sum(digitos[0::2])
soma_pares = 0
for d in digitos[1::2]:
    dobro = d * 2
    if dobro > 9:
        dobro -= 9
    soma_pares += dobro

total = soma_impares + soma_pares

if total % 10 == 0:
    print("Cartão válido")
else:
    print("Cartão inválido") com o número do cartão
numero = input()

# TODO: implemente a verificação pelo algoritmo de Luhn
# Siga as dicas do README.

# Ao final, imprima exatamente:
# print("Cartão válido")  ou  print("Cartão inválido")
