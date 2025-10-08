start_programa = True
recebe_campos = True
PI = 3.14159

while start_programa:
    while recebe_campos:
        try:
            raio = float(input("Digite o Raio da Circunferência: ").replace(",", "."))
            recebe_campos = False
        except:
            print("Campo inválido...")
    else:
        circ = 2 * PI * raio
        print("\n####### RETORNO DOS DADOS #########\n")
        print("O valor da circunferência é de ", circ, " mts")

        fim_programa = True
        while fim_programa:
            print("Deseja finalizar o programa?")
            confirma = str(input("Digite S (SIM) ou N (Novo Cálculo): "))
            if confirma == "s" or confirma == "S":
                fim_programa = False
                start_programa = False
            elif confirma == "n" or confirma == "N":
                fim_programa = False
                recebe_campos = True
else:
    print("\n>>>>>>>>> PROGRAMA FINALIZADO <<<<<<<<<<<<<\n")
