# metacaracteres:
# ^ -> começa com
# $ -> termina com
#[^a-z] -> negação
# \w -> [a-zA-Z0-9À-ú_]+   -> flags = re.A
# \w -> [^a-zA-Z0-9_] -> flags = re.A
# \d -> [0-9] 
# \D -> [^]
# \s -> [\R\n\f\t]
# \b -> borda
# \B -> não borda
#letras maiuculas é negação minusculas encontra
#re.A -> ASCII
#re.I -> IGNORECASE
#re.M -> Multiline ^|$ -> começa com e termina com
#re.S -> Dotall
#
#

import re

#cpf = '147.852.963-12'
#print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
#print(re.findall(r'[^0-9]+', cpf))

#texto = '''
#João trouxe     flores para sua amada namorada em 10 de janeiro de 1970,
#Maria era o nome dela.
#
#foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
#maria, hoe sua esposa ainda faz aquele café com pão de queijo nas tardes de
#domingos. Também né! sendo a boa mineira que é, nunca esquece seu famoso pão de queijo.
#Não canso de ouvir a Maria:
#"Jooooooooaãooooooo, o café ta pronto aqui, veeemm!"
#'''

#print(re.findall(r'[a-z]+', texto, flags=re.I ))
#print(re.findall(r'[a-zA-Z0-9]+', texto))
#print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))
#print(re.findall(r'\W+', texto)) #tras as palavras acentuadas
#print(re.findall(r'\d+', texto, flags=re.I))
#print(re.findall(r'\s+', texto, flags=re.I))
#print(re.findall(r'\b\w{4}\b', texto, flags=re.I))
#print(re.findall(r'\b\w{4}\b', texto, flags=re.I))

texto = '''
131.768.460-53
055.123.060-50
955.123.060-90
'''

#print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}', texto,flags=re.M))

texto2 = 'o João gosta de folia \n E adora ser amado'

print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S))