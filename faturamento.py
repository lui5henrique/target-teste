import json

def carregar_dados(filename):
    with open(filename, 'r') as file:
        dados = json.load(file)
    return dados

def calcular_faturamento(dados):
    valores = [dia['valor'] for dia in dados if dia['valor'] != 0.0]
    
    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    
    dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_da_media

def main():
    dados = carregar_dados('faturamento.json')
    
    menor_valor, maior_valor, dias_acima_da_media = calcular_faturamento(dados)
    
    print(f"Menor valor de faturamento: {menor_valor:.2f}")
    print(f"Maior valor de faturamento: {maior_valor:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

if __name__ == "__main__":
    main()
