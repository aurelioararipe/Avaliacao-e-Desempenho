# ADS LISTA 6
# Aurelio Chaves Araripe
# Simulador fila de banco

import random

class Cliente:
    def __init__(self, numCliente):
        self._numCliente = numCliente
        self.tempoChegada = 0
        self.tempoAtendimento = 0
        self.tempoInicioServico = 0
        self.tempoFila = 0
        self.tempoFinalAtendimento = 0
        self.tempoTotalBanco = 0

    def geradorTempoAtendimento(self):
        peso_tempos = [(9, 30), (10, 50), (11, 20)]
        lista_tempos = [tempo for tempo, peso in peso_tempos for i in range(peso)]
        return random.choice(lista_tempos)

    def geradorTS(self, random_number):
        if 0.00 <= random_number and random_number <= 0.06:
            return 9.275
        elif 0.07 <= random_number and random_number <= 0.11:
            return 9.825
        elif 0.12 <= random_number and random_number <= 0.34:
            return 10.375
        elif 0.35 <= random_number and random_number <= 0.54:
            return 10.925
        elif 0.55 <= random_number and random_number <= 0.75:
            return 11.475
        elif 0.76 <= random_number and random_number <= 0.87:
            return 12.025
        elif 0.88 <= random_number and random_number <= 0.96:
            return 12.575
        elif random_number == 0.97:
            return 13.125
        elif 0.98 <= random_number and random_number <= 0.99:
            return 13.675
        elif 1.00 == random_number:
            return 14.225

class Banco:
    def __init__(self):
        self.tempoUltimaChegada = []
        self.tempoLivreCaixa = 0

    def geradorChegadas(self):
        peso_tempos = [(10, 35), (12, 40), (14, 25)]
        lista_tempos = [tempo for tempo, peso in peso_tempos for i in range(peso)]
        return random.choice(lista_tempos)

    def geradorTEC(self, random_number):
        if 0.00 <= random_number and random_number <= 0.35:
            return 2.5
        elif 0.36 <= random_number and random_number <= 0.54:
            return 7.5
        elif 0.55 <= random_number and random_number <= 0.73:
            return 12.5
        elif 0.74 <= random_number and random_number <= 0.86:
            return 17.5
        elif 0.87 <= random_number and random_number <= 0.89:
            return 22.5
        elif 0.90 <= random_number and random_number <= 0.96:
            return 27.5
        elif random_number == 0.97:
            return 32.5
        elif 0.98 <= random_number and random_number <= 0.99:
            return 37.5
        elif 1.00 == random_number:
            return 42.5

    def caixaLivre(self, tempoFinalAtendimento, tempoChegada):
        if tempoChegada > tempoFinalAtendimento:
            self.tempoLivreCaixa = tempoChegada - tempoFinalAtendimento



def processo(opcao):
    print("TU = Tempo da ultima chegada")
    print("TC = Tempo de chegada no relogio")
    print("TA = Tempo de atendimento")
    print("TI = Tempo de inicio do servico")
    print("TF = Tempo de fila")
    print("TFA = Tempo de final de atendimento no relogio")
    print("TB = Tempo total no banco")
    print("TL = Tempo do caixa livre")
    print()
    print("CL |   TU   |   TC   |   TA   |   TI   |   TF   |   TFA   |   TB   |   TL  ")
    clientes = []
    bb = Banco()

    cont = 1
    while cont <= 20:
        cli = Cliente(cont)
        #Gerando TEMPO DE CHEGADA e TEMPO ATENDIMENTO

        if opcao == 1: #ITEM A
            chegada_random = bb.geradorChegadas()
            atendimento_random = cli.geradorTempoAtendimento()
        else: #ITEM B
            chegada_random = bb.geradorTEC(round(random.uniform(0,1),2))
            atendimento_random = cli.geradorTS(round(random.uniform(0, 1), 2))

        cli.tempoAtendimento = atendimento_random
        bb.tempoUltimaChegada.append(chegada_random)

        # TEMPO CHEGADA CLIENTE
        if cont == 1:
            cli.tempoChegada = bb.tempoUltimaChegada[cont - 1]
        else:
            cli.tempoChegada = bb.tempoUltimaChegada[cont - 1] + clientes[cont - 2].tempoChegada

        # TEMPO DE FILA, caso caixa esteja ocupado
        if cont != 1:
            if cli.tempoChegada < clientes[cont - 2].tempoFinalAtendimento:
                cli.tempoFila = clientes[cont - 2].tempoFinalAtendimento - cli.tempoChegada
            else:  # TEMPO CAIXA LIVRE
                bb.caixaLivre(clientes[cont - 2].tempoFinalAtendimento, cli.tempoChegada)

        cli.tempoInicioServico = cli.tempoFila + cli.tempoChegada
        cli.tempoFinalAtendimento = cli.tempoChegada + cli.tempoFila + cli.tempoAtendimento

        cli.tempoTotalBanco = cli.tempoFila + cli.tempoAtendimento

        clientes.append(cli)

        if cont - 2 == -1: #Caso seja o primeiro cliente, o tempo da ultima chegada e zero
            print(cont, " |", end="")
            print("0.000", " |", end="")
            print("%.3f"%clientes[cont - 1].tempoChegada, " |", end="")
            print("%.3f"%clientes[cont - 1].tempoAtendimento, " |", end="")
            print("%.3f"%clientes[cont - 1].tempoInicioServico, " |", end="")
            print("%.3f"%clientes[cont - 1].tempoFila, " |", end="")
            print("%.3f"%clientes[cont - 1].tempoFinalAtendimento, "|", end="")
            print("%.3f"%clientes[cont - 1].tempoTotalBanco, " |", end="")
            print("%.3f"%bb.tempoLivreCaixa)
        else:
            print(cont, " |", end="")
            print("%.3f"%clientes[cont - 2].tempoChegada, " |", end="")
            print("%.3f"%clientes[cont - 1].tempoChegada, " |", end="")
            print("%.3f"%clientes[cont - 1].tempoAtendimento, " |", end="")
            print("%.3f"%clientes[cont - 1].tempoInicioServico, " |", end="")
            print("%.3f"%clientes[cont - 1].tempoFila, " |", end="")
            print("%.3f"%clientes[cont - 1].tempoFinalAtendimento, "|", end="")
            print("%.3f"%clientes[cont - 1].tempoTotalBanco, " |", end="")
            print("%.3f"%bb.tempoLivreCaixa)

        # print("tempo chegada: ", clientes[cont-1].tempoChegada)
        # print("tempo fila: ", clientes[cont - 1].tempoFila)
        # print("tempo inicio servico: ", clientes[cont-1].tempoInicioServico)
        # print("tempo atendimento: ", clientes[cont - 1].tempoAtendimento)
        # print("tempo final atendimento: ", clientes[cont-1].tempoFinalAtendimento)
        # print("tempo caixa livre: ", bb.tempoLivreCaixa)
        # print("---------------------")

        cont += 1

def options(num):
    if num < 3:
        processo(num)
    else:
        print("1 ou 2")

print("SIMULAÇÃO DE UM BANCO")
print("Escolha qual tipo de simulação")
print("1: Item A, sorteio de valores com probabilidades diferentes")
print("2: Item B, Monte Carlo")
num = int(input())

options(num)