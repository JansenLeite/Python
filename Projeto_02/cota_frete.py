import mod_inputs

def cabecalho():
    print("#########################################")
    print("\n<<<<< Seja bem vindo ao Cota Frete >>>>>")
    print("#########################################")

def recebe_destino():
    num = mod_inputs.inp_int_destino("Informe o código do Aeroporto: ")
    return num

def recebe_embalagem():
    num = mod_inputs.inp_int_embalagem("Informe o código da Embalagem: ")
    return num

def recebe_altura():
    num = mod_inputs.inp_float("Informe a altura em Metros da Embalagem: ")
    return num

def recebe_largura():
    num = mod_inputs.inp_float("Informe a largura em Metros da Embalagem: ")
    return num

def recebe_profundidade():
    num = mod_inputs.inp_float("Informe a profundidade em Metros da Embalagem: ")
    return num

def recebe_peso():
    num = mod_inputs.inp_float("Informe peso em Kg da Embalagem: ")
    return num

def tabela_distancia(destino):
    match destino:
        case 1:
            distancia = 102
        case 2:
            distancia = 112
        case 3:
            distancia = 98
        case 4:
            distancia = 2922
        case 5:
            distancia = 6294
    return distancia

def calcula_frete(destino, embalagem, altura, largura, profundidade, peso):
    match embalagem:
        case 1:
            fator = 0.26
        case 2:
            fator = 0.37
    
    distancia = tabela_distancia(destino)