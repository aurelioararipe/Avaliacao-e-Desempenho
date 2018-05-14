# ADS LISTA 7
# Aurelio Chaves Araripe
# Simulador fila de banco

import random
import math

class Cliente:
    def __init__(self, numCliente):
        self._numCliente = numCliente
        self.tempoChegada = 0
        self.tempoAtendimento = 0
        self.tempoInicioServico = 0
        self.tempoFila = 0
        self.tempoFinalAtendimento = 0
        self.tempoTotalBanco = 0

    def geradorTS(self, mean):
        n, P = 0, 1
        while True:
            P = P * random.uniform(0, 1)
            if P < math.exp(-mean):
                return float(n / 60)
            else:
                n = n + 1

class Banco:
    def __init__(self):
        self.tempoUltimaChegada = []
        self.tempoLivreCaixa = 0

    def geradorTEC(self, mean):
        return float((-1.0 / mean) * math.log(1 - random.uniform(0, 1)))

    def caixaLivre(self, tempoFinalAtendimento, tempoChegada):
        if tempoChegada > tempoFinalAtendimento:
            self.tempoLivreCaixa = tempoChegada - tempoFinalAtendimento



def processo():
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

        chegada_random = bb.geradorTEC(12)
        atendimento_random = cli.geradorTS(6)

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
            print("%.3f"%clientes[cont - 1].tempoChegada, "  |", end="")
            print("%.3f"%clientes[cont - 1].tempoAtendimento, "  |", end="")
            print("%.3f"%clientes[cont - 1].tempoInicioServico, "  |", end="")
            print("%.3f"%clientes[cont - 1].tempoFila, "  |", end="")
            print("%.3f"%clientes[cont - 1].tempoFinalAtendimento, " |", end="")
            print("%.3f"%clientes[cont - 1].tempoTotalBanco, "  |", end="")
            print("%.3f"%bb.tempoLivreCaixa)
        else:
            print(cont, " |", end="")
            print("%.3f"%clientes[cont - 2].tempoChegada, "  |", end="")
            print("%.3f"%clientes[cont - 1].tempoChegada, "  |", end="")
            print("%.3f"%clientes[cont - 1].tempoAtendimento, "  |", end="")
            print("%.3f"%clientes[cont - 1].tempoInicioServico, "  |", end="")
            print("%.3f"%clientes[cont - 1].tempoFila, "  |", end="")
            print("%.3f"%clientes[cont - 1].tempoFinalAtendimento, " |", end="")
            print("%.3f"%clientes[cont - 1].tempoTotalBanco, "  |", end="")
            print("%.3f"%bb.tempoLivreCaixa)

        # print("tempo chegada: ", clientes[cont-1].tempoChegada)
        # print("tempo fila: ", clientes[cont - 1].tempoFila)
        # print("tempo inicio servico: ", clientes[cont-1].tempoInicioServico)
        # print("tempo atendimento: ", clientes[cont - 1].tempoAtendimento)
        # print("tempo final atendimento: ", clientes[cont-1].tempoFinalAtendimento)
        # print("tempo caixa livre: ", bb.tempoLivreCaixa)
        # print("---------------------")

        cont += 1

processo()