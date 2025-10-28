def inp_float(mensagem):
    valida = True
    while valida:
        try:
            inp = float(input(mensagem).replace(",", "."))
            valida = False
        except:
            print("Campo inválido!")
    return inp

def inp_str(mensagem):
    valida = True
    while valida:
        try:
            inp = str(input(mensagem))
            valida = False
        except:
            print("Campo inválido!")
    return inp

def inp_int(mensagem):
    valida = True
    while valida:
        try:
            inp = int(input(mensagem))
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

def inp_int_destino(mensagem):
    valida = True
    while valida:
        print("<<<<<< Informe o Aeroporto de Destino >>>>>>")
        print("1 - Congonhas-SP")
        print("2 - Guarulhos-SP")
        print("3 - Campo de Marte-SP")
        print("4 - Pinto Martins-CE")
        print("5 - Eduardo Gomes-AM")
        try:
            inp = int(input(mensagem))
            if inp == 1 or inp == 2 or inp == 3 or inp == 4 or inp == 5:
                valida = False
        except:
            print("Campo inválido!")
    return inp

def inp_int_embalagem(mensagem):
    valida = True
    while valida:
        print("<<<<<< Informe o Tipo de Embalagem >>>>>>")
        print("1 - Caixa de Papelão")
        print("2 - Container")
        try:
            inp = int(input(mensagem))
            if inp == 1 or inp == 2:
                valida = False
        except:
            print("Campo inválido!")
    return inp