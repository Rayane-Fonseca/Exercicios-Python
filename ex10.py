#esse vai pedir ao usuário os números

altura = int (input("Digite a Altura: "))
base = int (input("Digite a Medida da Base: "))

resultado = altura * base
print (f"A área do retângulo é de: {resultado}")

#esse já tem os números armazenados dentro do código

def area (base, altura):

    resultado = base * altura
    print(f"A área do retângulo é: {resultado}")

base = int (input("Digite a base do rêntangulo: "))
altura = int (input("Digite a altura: "))

#chamar a função
area (base, altura)