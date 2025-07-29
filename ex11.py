#esse vai pedir ao usuário os números

numeroum = int (input("Digite o primeiro número: "))
numerodois = int (input("Digite o segundo número: "))

soma = numeroum + numerodois
print (f"Resultado da Soma: {soma}")

multiplicacao = numeroum * numerodois
print (f"Resultado da multiplicação: {multiplicacao}")

#esse já tem os números armazenados dentro do código

def soma_produto (a,b):
    print(f"Soma: {a+b}")
    print(f"Produto: {a*b}")

soma_produto (2,8)
