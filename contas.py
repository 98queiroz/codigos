from abc import ABC, abstractmethod
from cliente import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        
        self.saldo -= valor
        self.detalhes()

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()