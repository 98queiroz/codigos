def leiaString():
    import re
    comando = False
    while not comando:
        try:
            txt = str(input('Digite seu nome: ')).strip()
            print(bool(re.search(r'\d',txt) or txt ==''))
            
        except(ValueError, TypeError):
            return 0
        else:
            comando = True
            return txt
