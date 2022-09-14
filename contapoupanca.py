from contaclass import Conta

class ContaPoupanca(Conta):
    
    #metodo sobreposto
    def sacar(self,valor):
        if self._saldo < valor:
            print('saldo insuficiente')
            return

        self._saldo -= valor
        self.detalhes()