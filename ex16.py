#Crie um programa que peça ao usuário para digitar seu nome e 
#sua idade. Imprima uma mensagem endereçada a ele que diga em 
#que ano ele completaá 100 anos.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

sub = 100 - idade
ano = sub + 2025

print (f"Olá {nome} o ano que você completará 100 anos será: {ano}")

#usando importação

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

from datetime import datetime

ano_atual = datetime.now().year
ano_cem = ano_atual + (100 - idade)

print (f"Olá {nome} o ano que você completará 100 anos será: {ano}")