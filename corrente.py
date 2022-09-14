from tkinter.filedialog import SaveFileDialog


class ContaCorrente:
    def __init__(self, numero) -> None:
        self._numero = numero
        self._saldo = 0
        self._status = 'especial'
        self._limite = 500
        self._limiteUsado = ''
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, valor):
        if isinstance(valor, str):
            print('favor de colocar um numero inteiro')
            return    
        self._valor = valor
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, bol):
        if not isinstance(bol, bool):
            print('favor de colocar True ou False')
        
        self._status = bol

    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, valor):
        if not isinstance(valor, float):
            print('favor digite um numero float')

        self._limite = valor
    @property
    def limiteUsado(self):
        return self._limiteUsado
    
    @limiteUsado.setter
    def limiteUsado(self,valor):
        if not isinstance(valor, float):
            print('digite um float')
        
        self._limiteUsado = valor


    def realizar_saque(self, valor):

        #se tem saldo na conta
        if self._saldo >= valor:
            self._saldo -= valor
            return True

        #se é especial
        #verificar se tem limite
        elif self._status == 'especial':
            self._limiteUsado = self._limite + self._saldo
            if self._limiteUsado >= valor:
                self._saldo -= valor
                return True
        else:
            return False 
            #não é especial
    def realizar_deposito(self, valor):
        
        self._saldo += valor


        
    def consulta_dados(self):
        print('\t-- CONTRA-CHEQUE --')
        print(f'''numero conta: {self._numero}\nsaldo: {self._saldo}\nlimite disponivel: {self._limite}\nestatus: {self._status}
        ''')