class Escritor:
    def __init__(self, nome) -> None:
        self.__nome = nome
        self.__ferramenta = None

    #getter
    @property
    def nome(self):
        return self.__nome
    
    #getter
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    #setter
    @nome.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca) -> None:
        self.__marca = marca
    
    @property
    def marca(self):
        return self.__marca
    
    def escrever(self):
        print('Caneta Está escrevendo...')


class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina está escrevendo...')