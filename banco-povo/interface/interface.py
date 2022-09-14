#futuramente melhorar a tela de login com comprimento de senha


#dados do usuario local
login_usuarios = {'login':'queiroz', 'senha':1234}

cont = 0
while True:
    try:
        usuario = str(input('\033[33mDigite seu login: \033[m')).lower().strip()
        senha = int(input('\033[33mDigite sua senha: \033[m').strip())

        if usuario == login_usuarios['login'] and senha == login_usuarios['senha']:
            print(f"\033[36mBem vindo ao banco do povo Sr: {login_usuarios['login']}\033[m")
            break
        else:
            print('\033[31mfavor digitar login e senha corretamente!\033[m')
            cont += 1
            if cont == 3:
                print('ATÉ BREVE....')
                break
    except ValueError:
        print('digite apenas texto sem caracter especiais.')
        continue
    except KeyboardInterrupt:
        print('-- ATÉ LOGO! --')
        break