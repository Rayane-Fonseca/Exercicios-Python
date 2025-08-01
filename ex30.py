def analisa_salarios(*salarios):
    if not salarios:
        print("Nenhum salário informado.")
        return

    media = sum(salarios) / len(salarios)
    menor = min(salarios)
    maior = max(salarios)
    acima_media = sum(1 for s in salarios if s > media)
    total_pago = sum(salarios)

    print(f"Média salarial: {media:.2f}")
    print(f"Menor salário: {menor:.2f}")
    print(f"Maior salário: {maior:.2f}")
    print(f"Colaboradores acima da média salarial: {acima_media}")
    print(f"Total pago em salários: {total_pago:.2f}")

analisa_salarios(2500.00, 3000.00, 1500.00, 4000.50, 2300.10)