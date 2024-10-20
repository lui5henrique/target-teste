# Definir os valores de faturamento mensal por estado
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcular o valor total de faturamento mensal
total_faturamento = sum(faturamento.values())

# Calcular o percentual de representação de cada estado
percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento.items()}

# Imprimir os resultados
print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

# Output:
# Percentual de representação por estado:
# SP: 37.53%
# RJ: 20.29%
# MG: 16.17%
# ES: 15.04%
# Outros: 10.98%
