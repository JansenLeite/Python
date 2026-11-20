import pyfiglet

def msg_inicial():
    print("Seja bem vindo ao Sistema\n")
    mensagem = pyfiglet.figlet_format("COTA-FRETE", font="pagga")
    print(mensagem)

def msg_login_ini():
    print("##############################")
    print("<<<<<< LOGAR NO SISTEMA >>>>>>")
    print("##############################\n")

def msg_menu_principal():
    print("##########################################################")
    print("<<<<<<<<<<<<<<<<<<<< MENU PRINCIPAL >>>>>>>>>>>>>>>>>>>>>>")
    print("##########################################################\n")
    print("##### SAIR - 0 | CALCULADORA - 1 | CALCULA FRETE - 2 #####\n")

def msg_calc_ini():
    print("##############################")
    print("<<<<<<<< CALCULADORA >>>>>>>>>")
    print("##############################\n")
