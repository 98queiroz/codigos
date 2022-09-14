""" 
EM PYTHON TUDO É UM OBJETO:incluindo classes Metaclasses
são as "classes" que criam classes.
type é uma metaclasse (!!!????)

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        
        if 'attr_classe' in namespace:
            print(f'{name}, tentou sobrescrever o atributo.')
            del namespace['attr_classe']


        ''' if 'b_fala' not in namespace:
            print(f'oi, voce precisa criar o metodo b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um metodo, não atributo em {name}') '''

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = 'valor A'


class B(A):
    attr_classe = 'valor B'

class C(B):
    attr_classe = 'valor C'

c =C()
print(c.attr_classe) """

class Pai:
    nome = 'teste'

A = type('A', (Pai,), {'attr': 'ola mundo!'})

a = A()
print(a.nome)