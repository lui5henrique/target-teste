def inverter_string(s):
    # Inicializa uma string vazia para armazenar o resultado
    resultado = ""
    # Itera sobre a string original de trás para frente
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    return resultado

def main():
    # Informe a string a ser invertida aqui
    string_original = input("Informe a string a ser invertida: ")
    
    string_invertida = inverter_string(string_original)
    
    print(f"String original: {string_original}")
    print(f"String invertida: {string_invertida}")

if __name__ == "__main__":
    main()
