'''crie uma função para desenhar uma linha, usando o caractere _ 
o tamanho da linha deve ser definido na chamada da função'''

def linha(n):
    for i in range(n):
        print(end="__")
        #end: controla o que é impresso na mensagem ao final da tela
    print("")

linha(100)