import mod_msg
import mod_inputs
import mod_finaliza

def valida_operador():
    while True:
        print("Digite * para MULTIPLICAÇÃO")
        print("Digite / para DIVISÃO")
        print("Digite + para ADIÇÃO")
        print("Digite - para SUBTRAÇÃO\n")
        print("Digite % para PORCENTAGEM\n")
        operador = mod_inputs.recebe_str("Digite um operador: ")
        if operador in("*", "/", "+", "-", "%"):
            break
        else:
            print("\nOperador inválido!\n")
    return operador

def realiza_calculo(num1, num2, operador):
    match operador:
        case "*":
            resultado = num1 * num2  
        case "/":
            resultado = num1 / num2
        case "+":
            resultado = num1 + num2
        case "-":
            resultado = num1 - num2
        case "%":
            resultado = num1 * num2 / 100
    return resultado  

def mensagem_final(num1, num2, operador, resultado):
    if operador == "%":
        print(f"O resultado de {num1} {operador} de {num2} é = {resultado}")
    else:
        print(f"O resultado de {num1} {operador} {num2} é = {resultado}")


def main():
    start = True
    while start:
        mod_msg.msg_calc_ini()
        num1 = mod_inputs.recebe_float("Digite o primeiro número: ")
        num2 = mod_inputs.recebe_float("Digite o segundo número: ")
        operador = valida_operador()
        resultado = realiza_calculo(num1, num2, operador)
        mensagem_final(num1, num2, operador, resultado)
        start = mod_finaliza.finaliza_programa()

if __name__ == "__main__":
    main()
