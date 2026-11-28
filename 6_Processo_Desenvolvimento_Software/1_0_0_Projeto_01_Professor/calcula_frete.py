import mod_msg
import mod_inputs
import mod_finaliza

def recebe_opcao():
    while True:
        mod_msg.msg_ct_aeroporto()
        opcao = mod_inputs.recebe_int("Digite uma opção: ")
        if opcao in(0, 1, 2, 3, 4, 5):
            break
        else:
            print("Opção inválida!\n")
    return opcao

def escolhe_aeroporto(opcao):
    aeroporto = ["CONGONHAS/SP", "GUARULHOS/SP", "CAMPO DE MARTE/SP", "PINTO MARTINS/CE", "EDUARDO GOMES/AM"]
    return aeroporto[opcao-1]

def escolhe_distancia(opcao):
    distancia = [102, 112, 98, 2922, 6294]
    return distancia[opcao-1]

def escolhe_embalagem():
    while True:
        mod_msg.msg_ct_embalagem()
        tipo = mod_inputs.recebe_int("Digite um tipo de caixa: ")
        if tipo in(0, 1, 2):
            break
        else:
            print("Opção inválida \n")
    return tipo

def tipo_emb(tipo_embalagem):
    match tipo_embalagem:
        case 1:
            embalagem = "Caixa de Papelão"
        case 2:
            embalagem = "Caixa Container"
    return embalagem

def calcula_frete(distancia, tipo_embalagem):
    match tipo_embalagem:
        case 1:
            # Calculo caixa de papelão
            y = mod_inputs.recebe_float("Digite a altura em MTS: ")
            x = mod_inputs.recebe_float("Digite a largura em MTS: ")
            z = mod_inputs.recebe_float("Digite a profundidade em MTS: ")
            w = mod_inputs.recebe_float("Digite o peso em KG: ")
            f = 0.015
        case 2: 
            # Calculo container
            y = mod_inputs.recebe_float("Digite a altura em MTS: ")
            x = mod_inputs.recebe_float("Digite a largura em MTS: ")
            z = mod_inputs.recebe_float("Digite a profundidade em MTS: ")
            w = mod_inputs.recebe_float("Digite o peso em KG: ")
            f = 0.026
    
    cubagem = y * x * z * 166.67

    if cubagem >= w:
        peso_real = cubagem
    else:
        peso_real = w

    formula = peso_real * distancia * f
    
    return round(formula, 2)    


def main():
    start = True
    while start:
        opcao = recebe_opcao()

        if opcao != 0:
            aeroporto = escolhe_aeroporto(opcao)
            distancia = escolhe_distancia(opcao)
            tipo_embalagem = escolhe_embalagem()
            embalagem = tipo_emb(tipo_embalagem)
            valor_frete = calcula_frete(distancia, tipo_embalagem)
            print("O aeroporto é: ", aeroporto)
            print("A distância é: ", distancia)
            print("O tipo de embalagem é: ", embalagem)
            print("O valor do Frete é: R$", valor_frete)
            start = mod_finaliza.finaliza_programa()
        else:
            break

if __name__ == "__main__":
    main()