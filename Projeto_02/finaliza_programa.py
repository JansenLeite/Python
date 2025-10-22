def finaliza_programa(mensagem):
    valida = True
    while valida:
        print("\nDeseja encerrar o programa?")
        try:
            confirma = str(input(mensagem))
            if confirma == "s" or confirma == "S":
                valida = False
                retorna = False
            elif confirma == "n" or confirma == "N":
                valida = False
                retorna = True
            else:
                print("Opção inválida...")
        except:
            print("Valor inválido...")
    return retorna
