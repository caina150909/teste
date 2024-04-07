def para_binario(texto):

    binarios = []
    for char in texto:
        ascii_valor = ord(char)

        binario = bin(ascii_valor)[2:]
        binarios.append(binario)
    return''.join(binarios)

entrada = input("digite a palavra ou numeros: ")

codigo_binario = para_binario(entrada)

print("o codigo binario de '{}' é: {}".format(entrada,codigo_binario))