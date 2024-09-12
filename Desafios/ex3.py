import json

with open('dados_faturamento.json', 'r') as file:
    dados = json.load(file)

faturamento_diario = [v for v in dados["faturamento_diario"].values() if v is not None]

menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)
media_mensal = sum(faturamento_diario) / len(faturamento_diario)
dias_acima_da_media = sum(f > media_mensal for f in faturamento_diario)

print(f"faturamento diário: {faturamento_diario}")
print(f"menor valor de faturamento: {menor_faturamento}")
print(f"maior valor de faturamento: {maior_faturamento}")
print(f"número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
