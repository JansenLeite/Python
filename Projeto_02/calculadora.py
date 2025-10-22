import mod_inputs
import finaliza_programa

def mensagem():
    print("\n############################################")
    print("<<<<<<<<< Seja bem vindo a Calculadora >>>>>")
    print("############################################\n")

def recebe_campo1():
    num = mod_inputs.inp_float("Digite o primeiro número: ")
    return num

def recebe_campo2():
    num = mod_inputs.inp_float("Digite o segundo número: ")
    return num

def recebe_operacao():
    opc = mod_inputs.inp_str_oper("Digite uma operação: ")
    return opc

def processa_calculo(num1, num2, opc):
    if opc == "x" or opc == "X":
        resultado = num1 * num2
    elif opc == "/":
        resultado = num1 / num2
    elif opc == "+":
        resultado = num1 + num2
    elif opc == "-":
        resultado = num1 - num2
    elif opc == "%":
        resultado = (num1 / 100) * num2
    return resultado

def exibe_resultado(resultado):
    print("\n<<<<<<<< Resultado >>>>>>>>>")
    print("O resultado é : ", resultado)

def main():
    sair_programa = True
    while sair_programa:
        num1 = recebe_campo1()
        num2 = recebe_campo2()
        opc = recebe_operacao()
        resultado = processa_calculo(num1, num2, opc)
        exibe_resultado(resultado)
        sair_programa = finaliza_programa.finaliza_programa("Digite S (Voltar ao Menu Principal) ou N (Novo Cálculo): ")


if __name__ == "__main__":
    main()


