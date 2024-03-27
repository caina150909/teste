def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def farenheit_para_celsius(farenheit):
    celsius = (farenheit - 32) * 5/9
    return celsius


print("ESCOLHA A OPÇÃO DE CONVERSÃO: ")
print("1. CELSIUS PARA FARENHEIT")
print("2. FARENHEIT PARA CELSIUS")
opcao = int(input("digite o numero da opção desejada: "))

if opcao == 1:
    celsius = float(input("digite a temperatura em celsius: "))
    print("a temperatura em fahrenheit é: ", celsius_para_fahrenheit(celsius))
elif opcao == 2:
    farenheit = float(input("digite a temperatura em fahrenheit: "))
    print("a temperatura em celsius é:", farenheit_para_celsius(farenheit))
else:
    print("opção invalida, por favor escolha entre 1 e 2.")
