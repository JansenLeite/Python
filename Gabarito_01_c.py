#c) Crie uma calculadora com as 4 operações matemáticas (Multiplicação, Soma, Subtração e Divisão);

start_programa = True
recebe_campos = True
campos = 1
while start_programa:
    while recebe_campos:
        match campos:
            case 1:
                try:
                    num1 = float(input("Informe o primeiro número: ").replace(",", "."))
                    campos += 1
                except:
                    print("Campo inválido...")

            case 2:
                try:
                    print("\n##### INFORME UMA OPERAÇÃO #####\n")
                    print("Digite X, para Multiplicar")
                    print("Digite /, para Dividir")
                    print("Digite +, para Somar")
                    print("Digite -, para Subtrair\n")
                    oper = str(input("Informe uma Operação acima: "))
                    if oper == "x" or oper == "X" or oper == "/" or oper == "+" or oper == "-":
                        campos += 1
                    else:
                        print("Operador inválido...")
                except:
                    print("Campo inválido...")
            case 3:
                try:
                    num2 = float(input("Informe o segundo número: ").replace(",", "."))
                    recebe_campos = False
                except:
                    print("Campo inválido...")

    else:

        if oper == "x" or oper == "X":
            resultado = num1 * num2
        elif oper == "/":
            resultado = num1 / num2
        elif oper == "+":
            resultado = num1 + num2
        elif oper == "-":
            resultado = num1 - num2
        else:
            resultado = "Você nao digitou um operador válido!"
        
        print("\n>>>>>>>>> RETORNANDO RESULTADO <<<<<<<<<<\n")
        print("O resultado é ", resultado)

        fim_programa = True
        while fim_programa:
            print("\nDeseja finalizar o Programa?\n")
            try:
                confirma = str(input("Digite S (SIM) ou N (Calcular Novamente): "))
                if confirma == "s" or confirma == "S":
                    fim_programa = False
                    start_programa = False
                if confirma == "n" or confirma == "N":
                    fim_programa = False
                    recebe_campos = True
                    campos = 1
            except:
                print("Opção inválida...")

else:
    print("\n######### Programa Finalizado ############\n")