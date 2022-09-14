from corrente import ContaCorrente

conta = ContaCorrente(332484)
conta._status = 'especial'

re = conta.realizar_saque(350)
if re:
    print('realizado com sucesso')
else:
    print('não foi possivel realizar o saque')
conta.consulta_dados()

re = conta.realizar_saque(150)
if re:
    print('realizado com sucesso')
else:
    print('não foi possivel realizar o saque')
conta.consulta_dados()


re = conta.realizar_saque(50)
if re:
    print('realizado com sucesso')
else:
    print('não foi possivel realizar o saque')
conta.consulta_dados()

conta.realizar_deposito(1500)
conta.consulta_dados()