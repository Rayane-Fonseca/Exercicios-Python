def dia_da_semana(dia):
    match dia:
        case "sábado" | "domingo":
            return "Fim de Semana"
        case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
            return "Dia útil"
        case _:
            return "Dia inválido!"

print(dia_da_semana("terça"))
print(dia_da_semana("ray"))