from finaliza_programa import finaliza_programa
class calculadora_simples:

    def recebe_dados(self):
        campos = 1
        while True:
            match campos:
                case 1:
                    try:
                        self.num1 = float(input("Informe o primeiro número: ").replace(",", "."))
                        campos += 1
                    except:
                        print("Erro: Campo inválido...")

                case 2:
                    try:
                        self.num2 = float(input("Informe o segundo número: ").replace(",", "."))
                        campos += 1
                    except:
                        print("Erro: Campo inválido...")

                case 3:
                    try:
                        print("\n####### OPERAÇÕES #######\n")
                        print("Digite X para multiplicar")
                        print("Digite / para dividir")
                        print("Digite + para somar")
                        print("Digite - para subtrair")
                        self.oper = str(input("Informe uma operação: ").replace(",", "."))
                        if self.oper == "x" or self.oper == "X" or self.oper == "/" or self.oper == "+" or self.oper == "-":
                            return False
                        else:
                            print("Operador inválido...")

                    except:
                        print("Erro: Campo inválido...")

    def processa_dados(self):
        match self.oper:
            case "X" | "x":
                self.resultado = self.num1 * self.num2
            case "/":
                self.resultado = self.num1 / self.num2
            case "+":
                self.resultado = self.num1 + self.num2
            case "-":
                self.resultado = self.num1 - self.num2

    def mostra_dados(self):
        print("\n###### Resultado #######")
        print("O resultado é ", self.resultado)

if __name__ == "__main__":
    carrega_classe = calculadora_simples()
    start_programa = True
    while start_programa:
        carrega_classe.recebe_dados()
        carrega_classe.processa_dados()
        carrega_classe.mostra_dados()
        start_programa = finaliza_programa()