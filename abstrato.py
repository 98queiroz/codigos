'''
abstrato - metodo abstrato - metodo que não tem corpo, cria metodo e não escreve o codigo
e herdam.

'''


from abc import ABC, abstractclassmethod, abstractmethod

class A(ABC):
    @abstractmethod
    def falar(self):
        ...

class B(A):
    def falar(self):
        print('falando.... B')

a = B()
a.falar()