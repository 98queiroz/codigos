#metacaracteres: . ^ $ * + ? {} [] \ | ()
# | -> significa ou
# . -> é qualquer caracter(com exceção da quebra de linha)
#[] -> conjunto de caracteres


import re

texto = '''
João trouxe     flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoe sua esposa ainda faz aquele café com pão de queijo nas tardes de
domingos. Também né! sendo a boa mineira que é, nunca esquece seu famoso pão de queijo.
Não canso de ouvir a Maria:
"Jooooooooaãooooooo, o café ta pronto aqui, veeem!"
'''

print(re.findall(r'João|Maria|ad....s', texto))
print(re.findall(r'João|joão|Maria', texto))
print(re.findall(r'[Jj]oão|[Mm]aria', texto))
print(re.findall(r'[a-z]aria', texto))
print(re.findall(r'[a-zA-Z0-9]aria', texto))