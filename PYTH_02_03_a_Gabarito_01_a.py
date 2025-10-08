# a) Criar um programa em Python onde o usuário irá digitar seu nome completo, idade e peso e ao final deverá mostrar todos os dados de forma personalizada. Considere que se o usuário tiver uma idade abaixo de 12 anos, mostre que ele é Criança. Se ele tiver uma idade acima de 12 e abaixo de 18 anos, ele é Adolescente. Se ele tiver uma idade acima de 17 anos e abaixo de 64 anos, ele é Adulto. E se ele tiver acima de 64 anos ele é Aposentado.
start_programa = True
start_campos = True
campo = 1
### Receber os Dados

while start_programa:
    while start_campos:

        match campo:
            case 1:
                try:
                    nome = str(input("Digite seu nome completo: "))
                    campo += 1
                except:
                    print("Valor nome inválido...")
            case 2:
                try:
                    idade = int(input("Digite sua idade em anos: "))
                    campo += 1
                except:
                    print("Idade inválida...")
            case 3:
                try:
                    peso = float(input("Digite seu peso em Kg: ").replace(",", "."))
                    start_campos = False
                except:
                    print("Peso inválido...")
    else:
        print("\n###### RETORNANDO DADOS #######\n")
        print("Seu nome é ", nome)
        print("Sua idade é ", idade, " anos.")
        print("Seu peso é ", peso, " Kgs")

        fim_programa = True
        while fim_programa:
            print("\nDeseja finalizar o programa?\n")
            try:
                confirma = str(input("Digite S (SIM) ou N (Finalizar): "))
                if confirma == "s" or confirma == "S":
                    fim_programa = False
                    start_programa = False
                elif confirma == "n" or confirma == "N":
                    fim_programa = False
                    start_campos = True
                    campos = 1
                else:
                    print("Valor inválido...")
            except:
                print("Campo inválido")
else:
    print("\n<<<<<<<<< PROGRAMA FINALIZADO >>>>>>>>>>>>\n")