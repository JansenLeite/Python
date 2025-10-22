def inp_float(mensagem):
    valida = True
    while valida:
        try:
            inp = float(input(mensagem).replace(",", "."))
            valida = False
        except:
            print("Campo inválido!")
    return inp

def inp_str_oper(mensagem):
    valida = True
    while valida:
        print("<<<<<< Informe uma operação >>>>>>")
        print("X para Multiplicação")
        print("/ para Divisão")
        print("+ para Adição")
        print("- para Subtração")
        print("% para Porcentagem")
        try:
            inp = str(input(mensagem))
            if inp == "X" or inp == "x" or inp == "/" or inp == "+" or inp == "-" or inp == "%":
                valida = False
        except:
            print("Campo inválido!")
    return inp