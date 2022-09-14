from banco_dados import carregar_contatos, guarda_contato
from typing import List, Dict
import os
import re
from tabulate import tabulate


def valNome():
    ok = False
    while True:
        try:
            nome = str(input('DIGITE SEU  NOME: ')).lower().strip()
             #utilizo duas expressões regulares, uma para substituir muitos espaços entre as strings para apenas
             # 1, e na outra expressão, um validador,para saber se está dentro dos requisitos.       
            nome = re.sub(r'\s+', ' ', nome)
            vdd = bool(re.findall(r'\d', nome))

            if vdd == True or nome == '':
                print('o campo está vazio ou contem numeros ou alfanumericos')
                ok = False
            else:
                ok = True
                return nome
            

        except (ValueError, TypeError):
            print('\033[31m-- POR FAVOR DIGITE APENAS CARACTERES --\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31m-- USUARIO PREFERIU NÃO DIGITAR --\033[m')
            nome = ''
            return nome


def valEmail():
    ok = False
    while True:
        try:
            emails = str(input('DIGITE SEU EMAIL: ')).lower().strip()
            #utilizo uma expressão regular para validar o meu campo de email, deve retornar True
            vdd = bool(re.findall('^\w+([.\-+!%l]\w+)*@\w+([.\-]\w+)+$', emails,flags=re.MULTILINE))

            if vdd == False or emails == '':
                print('o campo está vazio ou contem numeros ou alfanumericos')
                ok = False
            else:
                ok = True
                return emails
            

        except (ValueError, TypeError):
            print('\033[31m-- POR FAVOR DIGITE UM EMAIL VÁLIDO --\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31m-- USUARIO PREFERIU NÃO DIGITAR --\033[m')
            emails = ''
            return emails
            

def valTelefone(tele='', fla=True):
    ok = False

    while True:
        try:
            telefone = str(input('DIGITE SEU NUMERO NESTE FORMATO: ((xx) x xxxx-xxxx): ')).strip()
            vdd = bool(re.findall(r'^(\(\d{2}\)\s)(9\s)(\d{4}-\d{4})$',telefone, flags=re.I))

            if vdd:
                return telefone
            else:
                continue
        except (ValueError, TypeError):
            print('\033[31m-- POR FAVOR DIGITE UM NÚMERO INTEIRO --\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31m-- USUARIO PREFERIU NÃO DIGITAR --\033[m')
            telefone = ''
            return telefone
            

def cadastrar_user():
    #ponteiro onde carrega os dados na memoria, pode ser que seja a primeira vez cadastrando.
    lista_contatos = carregar_contatos()
    comando = 'continue'
    dados= {}
    ok = False

        
    while comando != 'n':
        nome = valNome()
        email = valEmail()
        telefone = valTelefone()

        #verificação para poder salvar no arquivo. apenas o email pode ser campo em branco.
        if nome and telefone == '' or nome == '' or telefone == '':
            print('FAVOR DIGITAR NOME E TELEFONE.')
            ok = True
            break

        dados = {"nome": nome, "email": email, "telefone": telefone}
        
        lista_contatos.append(dados.copy())
        dados.clear()
        print()

            

        comando = str(input('DESEJA CADASTRAR NOVAMENTE? [S/N]: '))
    if ok == False:
        guarda_contato(lista_contatos)
    os.system('cls')


def pesquisar_user(
    pessoas: List[Dict[str,str]])-> Dict[str,str]:

    try:
        nome= str(input('DIGITE SEU NOME ou EMAIL ou TELEFONE: '))
        user = procura_chave_user(pessoas,nome)
        imprimi_com_tabulate(user)
    except KeyboardInterrupt:
        print("\033[31m --ATÉ LOGO --\033[m")


#procura chave do usuario dentro do dicionario, fiz um typing para convert list para dict
def procura_chave_user(lista_contato: List[Dict[str,str]], nome: str) -> dict[str,str]:
    nomesContatos = []

    for user in lista_contato:
        if user["nome"].startswith(nome) or user["email"].startswith(nome) or user["telefone"].startswith(nome):
            nomesContatos.append(user.copy())
    return nomesContatos


def imprimi_com_tabulate(lista_contatos):
    table = []
    for nomes in lista_contatos:
        table.append([nomes['nome'],
                    nomes['email'],
                    nomes['telefone']
                    ])
    #ordenando a lista
    nova_table = sorted(table)
    print(tabulate(nova_table))

  
    

def alterar_user(
    pessoas: List[Dict[str,str]])-> Dict[str,str]:
    table = []
    print()
    print('\t\t---BEM VINDO---')
    print('PARA ATUALIZAR SEUS DADOS, DIGITE O NUMERO DE TELEFONE: ')

    try:
        tel = valTelefone()
        if tel =='':
            return
        print()
    
        resp = int(input('O QUE DESEJA ALTERAR: \033[36m [1] - NOME, [2] - EMAIL, [3] - TELEFONE: \033[m' ))
        if resp == 1:
            for pessoa in pessoas:
                nome, email, telefone = pessoa.values()
                if telefone == tel:
                    table.append(pessoa)
                    imprimi_com_tabulate(table)
                    pessoa['nome'] = valNome()
                    imprimi_com_tabulate(table)
            guarda_contato(pessoas)
                    
        if resp == 2:
            for pessoa in pessoas:
                nome, email, telefone = pessoa.values()
                if telefone == tel:
                    table.append(pessoa)
                    imprimi_com_tabulate(table)
                    pessoa['email'] = valEmail()
                    imprimi_com_tabulate(table)
            guarda_contato(pessoas)
                    
        if resp == 3:
            for pessoa in pessoas:
                nome, email, telefone = pessoa.values()
                if telefone == tel:
                    table.append(pessoa)
                    imprimi_com_tabulate(table)
                    pessoa['telefone'] = valTelefone()
                    imprimi_com_tabulate(table)
            guarda_contato(pessoas)

    except (ValueError, TypeError):
            print('\033[31m-- POR FAVOR DIGITE UM NÚMERO INTEIRO --\033[m')
    except KeyboardInterrupt:
            print('\033[31m-- USUARIO PREFERIU NÃO DIGITAR --\033[m')

    return '-- PESSOA NÃO ENCONTRADA --'







""" def imprimi_com_tabulate(lista_contatos):
    table = []
    for nomes in lista_contatos:
        table.append([nomes['nome'],
                    nomes['email'],
                    nomes['telefone']
                    ])
    print(tabulate(table)) """