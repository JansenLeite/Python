import mod_inputs
import calculadora

def menu():
    print("\nEscolha um programa:\n")
    print("Sair => 0 | Calculadora => 1 | Cota Frete => 2")

def recebe_menu():
    num = mod_inputs.inp_int("Informe o programa que deseja acessar: ")
    return num

def valida_menu(num):
    programa = True
    match num:
        case 0:
            programa = False
        case 1:
            calculadora.main()
        case 2:
            print("Chamar o Cota-Frete")
        case _:
            print("Menu inválido...")
    return programa

def main():
    executa = True
    while executa:
        menu()
        num = recebe_menu()
        executa = valida_menu(num)
    return executa

if __name__ == "__main__":
    main()