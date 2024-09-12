sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

faturamento_total = sp + rj + mg + es + outros

print("percentual de representação por estado:")
print(f"SP: {(sp / faturamento_total) * 100:.2f}%")
print(f"RJ: {(rj / faturamento_total) * 100:.2f}%")
print(f"MG: {(mg / faturamento_total) * 100:.2f}%")
print(f"ES: {(es / faturamento_total) * 100:.2f}%")
print(f"outros: {(outros / faturamento_total) * 100:.2f}%")
