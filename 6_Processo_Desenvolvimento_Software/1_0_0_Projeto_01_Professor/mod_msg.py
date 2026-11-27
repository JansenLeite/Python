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

def msg_final_programa():
    print("##############################################################")
    print("<<<<<<<< OBRIGADO POR UTILIZAR O PROGRAMA COTA-FRETE >>>>>>>>>")
    print("####################### VOLTE SEMPRE !!!!! ###################\n")

def msg_ct_aeroporto():
    print("#########################################################################################################")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< COTAÇÃO DE FRETE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("#########################################################################################################\n")
    print("SAIR - 0 | CONGONHAS/SP - 1 | GUARULHOS/SP - 2 | CAMPO DE MARTE/SP - 3 | PINTO MARTINS/CE - 4 | EDUARDO GOMES/AM - 5 \n")

def msg_ct_embalagem():
    print("#########################################")
    print("<<<< ESCOLHA UM TIPO DE EMBALAGEM >>>>>>>")
    print("#######################################\n")
    print("SAIR - 0 | PAPELÃO - 1 | CONTAINER - 2 \n")