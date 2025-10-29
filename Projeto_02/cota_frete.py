import finaliza_programa
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

    valor_frete = ((altura * largura * profundidade * peso) * (1 + fator)) * (1+(distancia * 9.8))

    return valor_frete

def mostra_cotacao(destino, embalagem, altura, largura, profundidade, peso, distancia, valor_frete):
    print("<<<<<<<< COTAÇÃO DO FRETE >>>>>>>>>\n")
    print("Altura (Mts)                : ", altura)
    print("largura (Mts)               : ", largura)
    print("Profunidade (Mts)           : ", profundidade)
    print("Dimensão da Embalagem M³    : ", altura * largura * profundidade)
    print("Peso (Kg)                   : ", peso)
    print("Distância (KM)              : ", distancia)
    print("Valor do Frete (R$)         : ", valor_frete)

def main():
    sair_programa = True
    while sair_programa:
        cabecalho()
        destino = recebe_destino()
        embalagem = recebe_embalagem()
        altura = recebe_altura()
        largura = recebe_largura()
        profundidade = recebe_profundidade()
        peso = recebe_peso()
        distancia = tabela_distancia(destino)
        valor_frete = calcula_frete(destino, embalagem, altura, largura, profundidade, peso)
        mostra_cotacao(destino, embalagem, altura, largura, profundidade, peso, distancia, valor_frete)
        sair_programa = finaliza_programa.finaliza_programa("Digite S (Voltar ao Menu Principal ou N (Nova Cotação de Frete): )")
    return sair_programa

if __name__ == "__main__":
    main()