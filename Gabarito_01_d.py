#Lembre-se de que o resultado do programa deverá retornar o nome do cliente, idade, peso, valor do IMC e Classificação.

start_programa = True
recebe_campos = True
campos = 1

while start_programa:
    while recebe_campos:
        match campos:
            case 1:
                try:
                    nome = str(input("Digite o nome do cliente: "))
                    campos += 1
                except:
                    print("Campo inválido...")

            case 2:
                try:
                     idade = int(input("Digite a idade em anos do cliente: "))
                     campos += 1
                except:
                    print("Campo inválido...")

            case 3:
                try:
                     peso = float(input("Digite o peso em Kg do cliente: "))
                     campos += 1
                except:
                    print("Campo inválido...")

            case 4:
                try:
                     altura = float(input("Digite a altura do cliente: "))
                     recebe_campos = False
                except:
                    print("Campo inválido...")


       
    else:

        imc = peso / altura ** 2

        if idade >= 20 and idade < 61:
            if imc < 18.5:
                classificacao = "Baixo Peso"
            elif imc >= 18.5 and imc <= 24.99:
                classificacao = "Normal"
            elif imc >= 25 and imc <= 29.99:
                classificacao = "Sobrepeso"
            else:
                classificacao = "Obesidade"

        elif idade > 60:
            if imc < 22:
                classificacao = "Baixo Peso"
            elif imc >= 22 and imc <= 27:
                classificacao = "Normal"
            elif imc > 27 and imc <= 29.99:
                classificacao = "Sobrepeso"
            else:
                classificacao = "Obesidade"


            print("O nome do cliente é ", nome)

            # idade
            print("A idade do cliente é ", idade)

            # peso
            print("O peso do cliente é ", peso, "Kgs")

            # valor do IMC 
            print("O IMC do cliente é ", imc)

            # Classificação.
            print("Sua classificação é ", classificacao)

            fim_programa = True
            while fim_programa:
                print("\nDeseja finalizar o Programa?\n")
                try:
                    confirma = str(input("Digite S (SIM) ou N (Calcular Novamente): "))
                    if confirma == "s" or confirma == "S":
                        fim_programa = False
                        start_programa = False
                    if confirma == "n" or confirma == "N":
                        fim_programa = False
                        recebe_campos = True
                        campos = 1
                except:
                    print("Opção inválida...")
else:
    print("Programa Finalizado")