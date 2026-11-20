import getpass

def recebe_str(mensagem):
    while True:
        try:
            texto = str(input(mensagem))
            break
        except:
            print("Valor inválido!")
    return texto

def recebe_senha(mensagem):
    while True:
        try:
            #senha = str(input(mensagem))
            senha = getpass.getpass(mensagem)
            break
        except:
            print("Valor inválido!")
    return senha

def recebe_int(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            break
        except:
            print("Valor inválido!")
    return numero

def recebe_float(mensagem):
    while True:
        try:
            numero = float(input(mensagem).replace(",", "."))
            break
        except:
            print("Valor inválido!")
    return numero