'''
assoiação - usa
agregação - tem
composição - é dono
herança - É
'''
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    
    def falar(self):
        print(f'{self.nomeclasse} Falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')
    
    def falar(self):
        print('Estou em cliente.')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')

class ClienteVip(Cliente):
    #sobreposição de metodos.
    #def falar(self):
        #Pessoa.falar(self) -> maneira de chamar o metodo da classe especifica
        #Cliente.falar(self) -> maneira de chamar o metodo da classe especifica
        #super().falar() # chamando o metodo da classe pai
       # print('outra coisa qualquer')
    def __init__(self, nome, idade,sobrenome) -> None:
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome
    
    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome}{self.sobrenome}')