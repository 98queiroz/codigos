#metacaracter: ^$( )
# * -> 0 ou N vezes -> pode ou não existe o caracter
# + -> 1 ou N vezes -> só substitui se existir o caracter
# ? -> 0 ou 1 vezes -> pode ou não existi o caracter
#{n} -> especifica quantidades de vezes
#{min, max} -> de vezes
#{10,} -> 10 ou mais repetições
#{,10} -> de zero a 10
#{10} -> especificamente 10
#{5,10} -> de 5 a 10 vezes

import re

texto = '''
João trouxe     flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoe sua esposa ainda faz aquele café com pão de queijo nas tardes de
domingos. Também né! sendo a boa mineira que é, nunca esquece seu famoso pão de queijo.
Não canso de ouvir a Maria:
"Jooooooooaãooooooo, o café ta pronto aqui, veeemm!"
'''

print(re.findall(r'j[a-zA-Z]ão+', texto, flags=re.IGNORECASE))
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.IGNORECASE))
print(re.findall(r've{3}m{1,2}', texto, flags=re.IGNORECASE))
# print(re.sub(r'jo{1,}ão{1,}', 'Felipe', texto, flags=re.IGNORECASE))

texto2 = 'João ama ser amado'
print(re.findall(r'ama[do]{2}',texto2, flags=re.I))