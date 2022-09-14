"""
o que são dataclasses? o modulo dataclasses fornece um decorador
e funlçoes para criar automaticamente métodos, como __init__(), __repr__(),
__eq__()etc em classes definidas pelo usuário.
Basicamente, dataclasses são synax sugar para cirar classes normais.
Foi originalmente descrito na pep 557.
adiconando a versão 3.7 do Python.
Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""
from codecs import ascii_decode
from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple

@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(
                f'tipo inválido {type(self.nome).__name__} != str em {self}'
            )

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

p1 = Pessoa('a', '5')
p2 = Pessoa('c', '3')
p3 = Pessoa('d', '4')
p4 = Pessoa('e', '6')

pessoas = [p1, p2, p3, p4]

print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome, reverse=True))
print(p1)

#print(p1)
#print(p1 == p2)

#print(p1.nome)
#print(p1.sobrenome)
#print(p1.nome_completo)

print()
print(asdict(p1))
print(astuple(p1))