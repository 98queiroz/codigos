'''
class Arquivo:
    def __init__(self, arquivo, modo):
        print('abrindo arquivo')
        self.arquivo = open(arquivo, modo)
    
    def __enter__(self):
        print('retornando arquivo')
        return self.arquivo
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('fechando arquivo')
        self.arquivo.close()
        #tratar a exceção se caso der algo errado aqui.


with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('alguma coisa')'''

from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        print(' abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('fechando arquivo')
        arquivo.close()

with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.write('linha 3\n')