'''
Exercicio com Abstração, Herança, encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e um banco.
A ideia é que o cliente tenha uma conta (poupança ou corernte) e que possa casar/depositar nessa conta. Contas corrente
tem um limite extra. Banco tem clientes e contas.

Dicas:
Criar classes Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupança)
Criar classes ContaPoupança e ContaCorrente que herdam de conta
    ContaCorrente deve ter um limite extra
    contas tem agencia, numero da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (abstração e polimorfismo -  as
    subclasses que implementam o método sacar)
Criar classe banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente  e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * checar se a agência é daquele banco
    * checar se o cliente é daquele banco
    * checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
'''

from banco import Banco
from cliente import Cliente
from contas import ContaCorrente,ContaPoupanca

banco = Banco()

cliente1 = Cliente('luiz', 30)
cliente2 = Cliente('maria', 18)
cliente3 = Cliente('joão', 50)

conta1 = ContaPoupanca(1111,254136, 0)
conta2 = ContaCorrente(2222,254137, 0)
conta3 = ContaPoupanca(1212,254138, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)


if banco.autenticar(cliente1):
    cliente1.conta.depositar(0)
    cliente1.conta.sacar(20)
else:
    print('cliente não autenticado.')

print('#############################')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print('cliente não autenticado.')