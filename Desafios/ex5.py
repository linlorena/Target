def inverter_recursivo(s):
    if len(s) <= 1:
        return s
    return inverter_recursivo(s[1:]) + s[0]

entrada = input("digite a string: ")
resultado = inverter_recursivo(entrada)
print(f"string invertida: {resultado}")
