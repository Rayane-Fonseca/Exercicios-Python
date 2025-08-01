def ordenar_lista(*numeros):
    if not numeros:
        print("Nenhum número informado.")
        return

numeros = [10,50,30,60,70,40,20]
numeros.sort()
print(numeros)

# outra versão

def ordenar_lista(lista):
    if not lista:
        return[]
    
    lista_ordenada = sorted(lista)
    print(f"Lista ordenada: {lista_ordenada}")

lista = [20,40,80,70,60,10,30]
ordenar_lista(lista)

#lista_decrescente = sorted(lista, reverse=True)