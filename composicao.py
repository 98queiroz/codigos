'''
associação ->
agregação ->
composicao -> relação mais forte entre classes - uma classe vai ser dona de objetos de outra classe, se a classe principal for apagada
todos os objetos que a clsse principal usou vai ser apagada com ela. 
'''

class Cliente:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_enderco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade,estado))   #composicao

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')
    
class Endereco:
    def __init__(self,cidade, estado) -> None:
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')