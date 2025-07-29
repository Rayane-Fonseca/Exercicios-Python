#Faça um programa que leia um nome de usuário e sua senha
#e não aceite a senha igual ao nome do usuário, mostrando
# uma mensagem de erro e voltando a pedir as informações.

while True:
    
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    if senha.lower == usuario.lower:
        print("ERRO: a senha não pode ser igual o nome.")
    else:
        print("Cadastro realizado com sucesso!")
        break