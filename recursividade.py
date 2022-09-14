#identificar o caso base, é o ponto de parada
#para que não execute infinitamente

""" from traceback import print_tb
def fatorial(numero):
    if numero == 1:
        return 1

    return numero * fatorial(numero - 1)

def fatorial_for(numero):
    resultado = 1

    for i in range(1,numero+1):
        resultado = resultado * i

    return resultado

print(fatorial_for(5)) """

import os

def scanear_pasta(pasta_inicial,pasta='', nivel = 0):
    caminho = os.path.join(pasta_inicial, pasta)
    if not os.path.isdir(caminho):
        return

    arquivos = os.listdir(os.path.join(pasta_inicial, pasta))

    for arquivo in arquivos:
        print('\t'* nivel,'>',arquivo)
        scanear_pasta(caminho,arquivo, nivel+1)


caminho = 'D:\\'
scanear_pasta(caminho)