from itertools import count
import re

'''
findall - vai encontrar todas as ocorrencias que eu quero encontrar dentro do meu texto
search - vai encontrar qual a primeira ocorrencia no meu texto e qual local
sub - para substituir
compile - para compilar as expressoes regulares.

'''

string = 'este é um teste de teste expressão regulares'
print(re.search(r'teste2', string))
print(re.findall(r'teste',string))
print(re.sub(r'teste', 'ABCD',string, count=0)) # count usado para alterar apenas uma ocorrencia

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.sub('def', string))
print(regexp.findall(string))