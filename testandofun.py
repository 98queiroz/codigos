import json
import tabulate
from telefone.banco_dados import guarda_contato, carregar_contatos





 

contatos = {}
lista = []
res = 'n'

while res != 's':
    nome = input('digite seu nome: ')
    telefone = input('digite seu telefone: ')
    email = input('digite seu email: ')


    contatos[nome.lower()] = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    lista.append(contatos.copy())
    contatos.clear()

    res = input('deseja sair (S/N): ')
        




guarda_contato(lista)
car = carregar_contatos()