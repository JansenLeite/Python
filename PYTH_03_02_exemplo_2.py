def somar_dados(num1, num2):
    resultado = num1 + num2
    return resultado

def mostrar_dados(resultado):
    print("O valor da SOMA é ", resultado)

if __name__ == "__main__":
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    processa = somar_dados(num1, num2)
    mostrar = mostrar_dados(processa)