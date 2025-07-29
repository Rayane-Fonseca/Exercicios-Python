#Função anônima: função sem nome --> Lambda
#Lambda argumentos: expressão

quadrado = lambda x: x **2
#lambda é a palavra-chave que define a função anonima
#x é o argumento de entrada
#x**2 é a expressão de retorno
print(quadrado(5))

def quadrado(x):
    return x**2

par_ou_impar = lambda x: "Par" if x % 2 == 0 else "Impar"