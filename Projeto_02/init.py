import login
import menu_principal
import letreiro

print("\nSeja bem vindo ao sistema\n")
print(letreiro.banner_pagga("COTA-FRETE"))
acesso = login.main()
if acesso:
    menu_principal.main()

print("\n<<<<<< Obrigado por utilizar o sistema COTAFRETE! Até a próxima! >>>>>>>>>>")