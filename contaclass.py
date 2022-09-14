from abc import ABC, abstractclassmethod, abstractmethod
from multiprocessing.sharedctypes import Value


class Conta(ABC):
    def __init__(self, agencia, conta, saldo) -> None:
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def conta(self):
        return self._conta
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('saldo precisa ser numerico')
        self._saldo = valor
    

        def depositar(self, valor):
            if not isinstance(valor, (int, float)):
                raise ValueError("valor do deposito precisa ser numerico")
            
            self._saldo += valor
            self.detalhes()
    
    def detalhes(self):
        print(f'agencia: {self._agencia}', end=' ')
        print(f'Conta: {self._conta}', end=' ')
        print(f'Saldo: {self._saldo}', end=' ')
    
    @abstractmethod
    def sacar(self, valor):
        ...