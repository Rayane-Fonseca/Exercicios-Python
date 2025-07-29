'''crie uma função estado_luz(status) que recebe uma string com o estado da luz: "ligado", "desligado", "piscando". use match case para retornar as mensagens'''

def estado_luz(status):

    match status:

        case "luz ligada":
            return "On"
        
        case "luz apagada":
            return "off"
        
        case "luz piscando":
            return "blink"
            
        case _:
            return "Estado desconhecido!"
        
print(estado_luz("luz apagada"))