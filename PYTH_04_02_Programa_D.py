from finaliza_programa import finaliza_programa
class calculo_imc:

    def recebe_dados(self):
        campos = 1
        while True:
            match campos:
                case 1:
                    try:
                        self.nome = str(input("Digite o nome do cliente: "))
                        campos += 1
                    except:
                        print("Campo inválido...")

                case 2:
                    try:
                        self.idade = int(input("Digite a idade em anos do cliente: "))
                        campos += 1
                    except:
                        print("Campo inválido...")

                case 3:
                    try:
                        self.peso = float(input("Digite o peso em Kg do cliente: "))
                        campos += 1
                    except:
                        print("Campo inválido...")

                case 4:
                    try:
                        self.altura = float(input("Digite a altura do cliente: "))
                        return False
                    except:
                        print("Campo inválido...")

    def processa_dados(self):
        self.imc = self.peso / self.altura ** 2

        if self.idade >= 20 and self.idade < 61:
            if self.imc < 18.5:
                self.classificacao = "Baixo Peso"
            elif self.imc >= 18.5 and self.imc <= 24.99:
                self.classificacao = "Normal"
            elif self.imc >= 25 and self.imc <= 29.99:
                self.classificacao = "Sobrepeso"
            else:
                self.classificacao = "Obesidade"

        elif self.idade > 60:
            if self.imc < 22:
                self.classificacao = "Baixo Peso"
            elif self.imc >= 22 and self.imc <= 27:
                self.classificacao = "Normal"
            elif self.imc > 27 and self.imc <= 29.99:
                self.classificacao = "Sobrepeso"
            else:
                self.classificacao = "Obesidade"
    
    def mostra_dados(self):
            print("O nome do cliente é ", self.nome)

            # idade
            print("A idade do cliente é ", self.idade)

            # peso
            print("O peso do cliente é ", self.peso, "Kgs")

            # valor do IMC 
            print("O IMC do cliente é ", self.imc)

            # Classificação.
            print("Sua classificação é ", self.classificacao)

if __name__ == "__main__":
    carrega_classe = calculo_imc()
    start_programa = True
    while start_programa:
        carrega_classe.recebe_dados()
        carrega_classe.processa_dados()
        carrega_classe.mostra_dados()
        start_programa = finaliza_programa()