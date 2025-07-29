'''contrua um programa que receba o nome e o preço de 5 medicamentos de uma drogaria (considere que o usuario 
informou cinco medicamentos distintos). o programa deve informar o nome e o preço do medicamento mais barato,
bem como a media aritimetica dos preços informados.'''

#criar vetor medicamentos
medicamentos = []

#receber nome e preço de 5 medicamentos
for i in range (5):
    nome = input(f"Digite o nome do {i+1}º medicamento: ")
    preco = float(input(f"Digite o preço do {i+1}º medicamento: R$ ")).replace(",",".") 
    #replace: substitui a vírgula por ponto
    medicamentos.append({"Nome": nome, "Preço": preco})
    
#informar o nome e o preço do medicamentos mais barato
mais_barato = min(medicamentos, key = lambda x: x['preco']) #lambda = função sem nome
