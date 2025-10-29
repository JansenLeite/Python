import mod_inputs
import calculadora
import cota_frete
import config
import letreiro

def menu():
    print(letreiro.banner_pagga("MENU PRINCIPAL"))
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
            cota_frete.main()
        case _:
            print("Menu inválido...")
    return programa

def main():
    executa = True
    while executa:
        config.limpa_tela()
        menu()
        num = recebe_menu()
        executa = valida_menu(num)
    return executa

if __name__ == "__main__":
    main()