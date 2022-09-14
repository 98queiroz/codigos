'''
public -> metodos e atributos que podem ser acessados por todos
protected -> metodos e atributos que só podem ser acessados de dentro da classe ou das filhas da classe
private -> atributo ou metodo que só pode ser acessado na classe

_privado/protected (public_)
__privado (_NOMECLASSE__nomeatributo)

setter = configurando um valor
getter = obter um valor (ler)





'''

class BaseDeDados:
    def __init__(self):
        self.__dados = {}
        
    def inserir_cliente(self,id,nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id:nome}
        else:
            self.__dados['clientes'].update({id:nome})
    
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]
        


bd = BaseDeDados() #instancia da classe
bd.inserir_cliente(1,'matheus')
bd.inserir_cliente(2,'queiroz')
#bd.lista_clientes()

print(bd.dados)