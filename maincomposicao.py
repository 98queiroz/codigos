from composicao import Cliente

cliente1 = Cliente('luiz', 32)
cliente1.inserir_enderco('belo horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('maria', 55)
cliente2.inserir_enderco('Salvador', 'BA')
cliente2.inserir_enderco('Rio de Janeiro','RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João', 19)
cliente3.inserir_enderco('Sao Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3