import math
from finaliza_programa import finaliza_programa
class calcula_circ:
    def recebe_dados(self):
        while True:
            try:
                self.raio = float(input("Digite o valor do Raio: ").replace(",", "."))
                return False
            except:
                print("Erro: Campo inválido...")

    def processa_circ(self):
        self.circ = 2 * math.pi * self.raio

    def mostra_circ(self):
        print("\n>>>>>>> RESULTADO <<<<<<<<\n")
        print("O valor da circunferência é => ", self.circ)

if __name__ == "__main__":
    carrega_classe = calcula_circ()
    start_programa = True
    while start_programa:
        carrega_classe.recebe_dados()
        carrega_classe.processa_circ()
        carrega_classe.mostra_circ()
        start_programa = finaliza_programa()