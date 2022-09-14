import json
import os


def carregar_contatos():
    lista_contato = []

    if os.path.exists('contatos.json'):
        with open('contatos.json', 'r') as f:
            lista_contato = json.load(f)
    return lista_contato


def guarda_contato(contatos):
    with open('contatos.json', 'w') as f:
        json.dump(contatos, f, indent=4)
        f.seek(0,2)

""" def listar_user():
    lista_contato = []

    if os.path.exists('contatos.json'):
        with open('contatos.json', 'r') as f:
            lista_contato = json.load(f)
    return lista_contato """