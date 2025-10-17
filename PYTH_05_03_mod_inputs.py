def inp_float(mensagem):
    valida = True
    while valida:
        try:
            inp = float(input(mensagem))
            valida = False
        except:
            print("Valor inválido...")
    return inp

def inp_str(mensagem):
    valida = True
    while valida:
        try:
            inp = str(input(mensagem))
            valida = False
        except:
            print("Valor inválido...")
    return inp

def inp_int(mensagem):
    valida = True
    while valida:
        try:
            inp = int(input(mensagem))
            valida = False
        except:
            print("Valor inválido...")
    return inp

def inp_str_oper(mensagem):
    valida = True
    while valida:
        print("<<<<<<   Informe uma operação >>>>>>")
        print("X para Multiplicação")
        print("/ para Divisão")
        print("+ para Adição")
        print("- para Subtração")
        print("% para Multiplicação")
        try:
            inp = str(input(mensagem))
            if inp == "X" or inp == "x" or inp == "/" or inp == "+" or inp == "-" or inp == "%":
                valida = False
        except:
            print("Valor inválido...")
    return inp