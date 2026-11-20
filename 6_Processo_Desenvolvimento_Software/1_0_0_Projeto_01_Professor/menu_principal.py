import mod_msg
import mod_inputs
import calculadora

def recebe_opcao():
    while True:
        opcao = mod_inputs.recebe_int("Digite uma opção do menu: ")
        match opcao:
            case 0:
                print("Sair do Programa!")
            case 1:
                #print("Aqui chamo a calculadora!")
                calculadora.main()
                break
            case 2:
                print("Aqui chamo Calcula Frete!")
            case _:
                print("Opção inválida!\n")

def main():
    while True:
        mod_msg.msg_menu_principal()
        recebe_opcao()
