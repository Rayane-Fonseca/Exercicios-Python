numeros = []

def ler_numeros ():

    soma = 0
    maior = None
    menor = None
    #None: nenhum valor / valor indefinido

    for i in range (10): 
        #range: gera uma sequencia de numeros inteiros no intervalo
        num = float (input(f"Digite o {i+1}º número: "))

        soma += num

        if maior is None or num > maior:
            maior = num

        if menor is None or num < maior:
            menor = num

    print (f"Soma dos números: {soma}")
    print (f"Maior número: {maior}")
    print (f"Menor número: {menor}")

ler_numeros ()
