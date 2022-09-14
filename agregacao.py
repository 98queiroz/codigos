'''
assosiação -> uma classe utiliza a outra classe mas que nenhuma das duas precisa
ncessariamente da outra classe, uma pode viver sem a outra.

agregação -> relação de todo parte - uma classe usa a outra como parte de si e essa classe precisa da outra classe.
carro e rodas, o carro existe sem o carro e as roda vivem sem o carro, mas não consegueria andar sem rodas.
composição ->
'''

class CarinhoDeCompra:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)
    
    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)
    
    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor) -> None:
        self.nome = nome
        self.valor = valor
