import mod_inputs

def recebe_campo1():
    num = mod_inputs.inp_float("Informe o primeiro número: ")
    return num
        
def recebe_campo2():
    num = mod_inputs.inp_float("Informe o segundo número: ")
    return num

def recebe_opcao():
    opc = mod_inputs.inp_str_oper("Digite uma operação: ")
    return opc

def processa_calculo(num1, num2, oper):
    if oper == "x" or oper == "X":
        resultado = num1 * num2
    elif oper == "/":
        resultado = num1 / num2
    elif oper == "+":
        resultado = num1 + num2
    elif oper == "-":
        resultado = num1 - num2
    elif oper == "%":
        resultado = num2 * (num1 / 100)
    return resultado

def imprime_dados(resultado):
    print("\n <<<<<<<< RESULTADO >>>>>>>>>>>>")
    print("O resultado é ", resultado)

def main():
    num1 = recebe_campo1()
    num2 = recebe_campo2()
    opc = recebe_opcao()
    resultado = processa_calculo(num1, num2, opc)
    imprime_dados(resultado)

if __name__ == "__main__":
    main()