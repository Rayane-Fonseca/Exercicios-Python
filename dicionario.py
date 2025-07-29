'''Dicionários são conjuntos de valores, onde '''

D = {"Arroz": 30.00, "Feijão": 9.00, "Alcatra": 45.00, "Alface": 3.00}
print (D)

print(D["Alcatra"])

for chave, valor in D.items():
    print(f"Chave: {chave} | Valor: {valor}")