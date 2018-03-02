import cmath

tempoMedio = 0
x = 0 # média
Nstr = 0 # quantidade de amostras
amostraStr = None
amostras = []
index = 0

#Nstr = input("Entre com o NUMERO de amostras ")
n = 33 #int(Nstr)

while index < n:
    amostraStr = input("Entre com a amostra ")
    amostras.append(int(amostraStr))
    tempoMedio = tempoMedio + amostras[index]
    index += 1
tempoMedio = tempoMedio/n
print("\ntempo médio = ", format(tempoMedio))

index = 0

#print(amostras)

# Calculo desvio padrao

S = 0
somatorio = 0
while index < n:
    somatorio += (amostras[index] - tempoMedio)*(amostras[index] - tempoMedio)
    print(round((amostras[index] - tempoMedio)*(amostras[index] - tempoMedio), 2), end=", ")
    index += 1
S = cmath.sqrt(somatorio / (n-1))

print("\n\nDesvio padrao = ", format(S))

# Calculo intervalo de confiança

#zStr = input("\nEntre com o valor da tabela normal ")
z = 1.645 #float(zStr)
menorIntervalo = 0
maiorIntervalo = 0

print(z*S/cmath.sqrt(n))
menorIntervalo = tempoMedio - (z*S/cmath.sqrt(n))
maiorIntervalo = tempoMedio + (z*S/cmath.sqrt(n))
print("\n\nMenor Intervalo = ", menorIntervalo)
print("Maior Intervalo = ", maiorIntervalo)


