
class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    #adicionando na lista
    def add(self, valor):
        self.__items.append(valor)
    
    #retornando a posição de um determinado valor
    def __getitem__(self, index):
        return self.__items[index]
    
    #atribuindo um valor a uma determinada posição
    def __setitem__(self, index, valor):
        if index >= len(self.__items):
            self.__items.append(valor)
        self.__items[index] = valor
    
    #deletando um valor da lista
    def __delitem__(self, index):
        del self.__items[index]
    
    #usando iterador
    def __iter__(self):
        return self

    #usando next com iterador
    #quando usado ele consome o iterador e no final gera um erro
    #neste caso tratamnos o erro.
    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
        except IndexError:
            raise StopIteration
        return item
    
    #mostrando na tela o nome da classe e a lista
    def __str__(self):
        return f'{self.__class__.__name__}({self.__items})'

    def __repr__(self):
        return self.__str__()

if __name__== '__main__':
    lista = MinhaLista()
    lista.add('Luiz')
    lista.add('maria')

    #lista = list(lista)

    """ print(lista)
    lista[0] = 'joao'
    lista[2] = 'funciona'
    del lista[2]

   
    print(lista) """

    for valor in lista:
        print(valor)
    
    print(lista)
    