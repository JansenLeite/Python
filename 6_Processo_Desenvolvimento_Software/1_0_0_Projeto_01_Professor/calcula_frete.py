import mod_msg
import mod_inputs

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

def main():
    start = True
    while start:
        opcao = recebe_opcao()
        if opcao != 0:
            aeroporto = escolhe_aeroporto(opcao)
            distancia = escolhe_distancia(opcao)
            print("O aeroporto é: ", aeroporto)
            print("A distância é: ", distancia)

        else:
            break

        
        #start = mod_finaliza.finaliza_programa()

if __name__ == "__main__":
    main()