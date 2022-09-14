from associacao import Escritor
from associacao import Caneta
from associacao import MaquinaDeEscrever

escritor = Escritor('Joaozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
#print(caneta.marca)

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()