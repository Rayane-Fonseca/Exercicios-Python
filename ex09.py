#esse vai pedir ao usuário os números

numero = int (input("Digite um número inteiro: "))
resultado = numero % 2

if resultado == 0:
    print (f"O número é par.")
else:
    print (f"O número é ímpar")

#esse já tem os números armazenados dentro do código
 
def e_par (n):

    if n % 2 == 0:
        print (True)
    else:
        print (False)

e_par (13)