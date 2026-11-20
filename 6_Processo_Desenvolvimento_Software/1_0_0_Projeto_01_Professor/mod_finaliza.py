import mod_inputs

def finaliza_programa():
    while True:
        print("\nDeseja encerrar o programa?\n")
        print("\nDigite S para encerrar o programa ou N realizar outro cálculo\n")
        confirma = mod_inputs.recebe_str("Digite uma opção: ")
        if confirma in("s", "S", "n", "N"):
            if confirma in("s", "S"):
                fim_programa = False
            else:
                fim_programa = True
            break
        else:
            print("\nOpção inválida!\n")
    return fim_programa