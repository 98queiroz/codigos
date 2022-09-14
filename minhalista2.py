from operator import delitem, index


class MinhaLista:
    #construtor da classe
    def __init__(self):
        self.__data = {}
        self.__index = 0
        self.__next_index = 0

    #adiciona os dados na lista
    #possivel desenpacotamento passando para o dicionario
    # assim: func('joao','maria')
    def add(self, *values):
        for value in values:
            self.__data[self.__index] = value
            self.__index += 1
    
    #verifica se a posição existe, caso não levanta uma raise
    def __check_index(self,index):
        if not self.__data.get(index):
            raise IndexError(f'Index {index} does not exist')
    
    #seta um valor no dicionario,lista asssim: lista[2]='pedro
    def __setitem__(self, index, value):
        self.__check_index(index)
        self.__data[index] = value
    
    #printa um determinado valor em tal posição
    #ex: print(lista[10])
    def __getitem__(self, index):
        self.__check_index(index)
        return self.__data[index]
    
    #magicmethod para deletar utilizando o del
    def __delitem__(self, index):
        self.__check_index(index)
        self.__data[index] = None
    
    #iterador - porem só funciona com os "next" enfim,
    #quem ler vai entender que é um iterador
    def __iter__(self):
        return self
    
    #responsavel por mostrar o proximo dado na varivel
    #ao finalizar ele retorna um erro, mas pode ser tratado
    #utilizando next ele não deixa "repetir" um for pois terá consumido o iterador
    def __next__(self):
        if self.__next_index >= self.__index:
            self.__next_index = 0
            raise StopIteration

        value = self.__data.get(self.__next_index)
        self.__next_index +=1
        return value

    #utilizado para poder dar um print no objeto
    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.__data}'
    
    

if __name__ == '__main__':
    lista = MinhaLista()
    lista.add('matheus0', 'joão')
    lista.add('helena')
    lista.add('julia')

    
    lista[0] = 'pedro'
    #del lista[0]

    for item in lista:
        print(item)

    for item in lista:
        print(item)

    