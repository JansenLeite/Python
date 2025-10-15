from finaliza_programa import finaliza_programa
class programa_recebe_dados:
    def receber_campos(self):
        campo = 1
        start_campos = True
        while start_campos:
            match campo:
                case 1:
                    try:
                        self.nome = str(input("Digite seu nome: "))
                        if len(self.nome) < 5:
                            print("Erro: O campo deve conter ao menos 5 caracteres!")
                        else:
                            campo += 1
                    except:
                        print("Campo inválido...")

                case 2:
                    try:
                        self.idade = int(input("Digite sua idade em anos: "))
                        campo += 1
                    except:
                        print("Campo inválido...")

                case 3:
                    try:
                        self.peso = float(input("Digite seu peso em Kg: ").replace(",", "."))
                        campo += 1
                        start_campos = False
                    except:
                        print("Campo inválido...")

    def mostrar_dados(self):
        print("Seu nome é ", self.nome)
        print("Seu peso é ", self.peso, " Kgs")
        print("Sua idade é ", self.idade, " anos")

if __name__ == "__main__":
    start_programa = True
    carrega_classe = programa_recebe_dados()
    while start_programa:
        carrega_classe.receber_campos()
        carrega_classe.mostrar_dados()
        start_programa = finaliza_programa()