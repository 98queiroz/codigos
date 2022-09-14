from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self,nome, idade):
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def inserir_conta(self, conta):
        self.conta = conta

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()
    

    def detalhes(self):
        print(f'agencia: {self.agencia}'
              f'Conta: {self.conta}'
              f'Saldo: {self.saldo}')
    
    @abstractmethod
    def sacar(self,valor):pass



