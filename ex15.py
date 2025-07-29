#desenvolva um programa em python que utilize while para permitir
#o cadastro de um número indeterminadode funcionários. o programa 
#deve encerrar o cadastro quando o usuario digitar 0 e, ao final, 
#exibir a lista completa dos funcionários registrados.

funcionarios = []

print("Cadastro de Funcionários")
print("Digite o nome do funcionário ou 0 para encerrar.")

while True:
    nome = input("Nome do funcionário: ")

    if nome == "0":
        break
    #break para parar quando reconhecer 0
    funcionarios.append(nome)

    if nome.strip() == "":
        print("Faltou o nome do funcionário")
    #remove opção em branco

print("\nLista de funcionários cadastrados:")
for i, funcionario in enumerate(funcionarios, start=1): 
    #enumerate (objeto a ser percorrido, valor inicial do índice)
    print(f"{i}. {funcionario}")

#outra forma sem enumerate

funcionarios = []

print("Cadastro de Funcionários")
print("Digite o nome do funcionário ou 0 para encerrar.")

while True:
    nome = input("Nome do funcionário: ")

    if nome == "0":
        break
    funcionarios.append(nome)

print("\nLista de funcionários cadastrados:")
for funcionario in funcionarios:
    print(f"Funcionário: {funcionario}")


