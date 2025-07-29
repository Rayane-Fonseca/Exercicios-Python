'''faça uma função dia_da_semana (número) que recebe um número de 1 a 7 e retorna o nome do dia da semana correspondente.'''

def dia_da_semana(dia):

    match dia:

        case "1":
            return "Segunda-Feira"
        
        case "2":
            return "Terça-Feira"
        
        case "3":
            return "Quarta-Feira"
        
        case "4":
            return "Quinta-Feira"
        
        case "5":
            return "Sexta-Feira"
        
        case "6":
            return "Sábado"
        
        case "7":
            return "Domingo"
        
        case _:
            return "Dia inválido!"
        
print(dia_da_semana("3"))


#fazendo para o usuario

def dia_da_semana(numero):

    match numero:

        case 1:
            return "Segunda-Feira"
        
        case 2:
            return "Terça-Feira"
        
        case 3:
            return "Quarta-Feira"
        
        case 4:
            return "Quinta-Feira"
        
        case 5:
            return "Sexta-Feira"
        
        case 6:
            return "Sábado"
        
        case 7:
            return "Domingo"
        
        case _:
            return "Dia inválido!"
        
entrada = int(input("Digite um número de 1 a 7: "))

resultado = dia_da_semana(entrada)

print(resultado)