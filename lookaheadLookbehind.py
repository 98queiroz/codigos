
#positive lookahed - verifica o que ta na frente para retornar determinada
#coisa que esta procurando a atras
#lookbehind - não retorna nada, quem retorna é a expressão regular



import re


msg = '''
ONLINE 192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE 192.168.0.4 GHIJK active
ONLINE 192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

#print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', msg))
#print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(\w+)', msg))
#print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', msg)) #positive lookahead
#print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', msg)) #negative lookahead
#print(re.findall(r'(?=.*active).+', msg)) #positive lookahead
#print(re.findall(r'(?=.*[^in]active).+', msg)) #negative lookahead

#positive lookbehind
#print(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', msg)) - tras todos os online
#negative lookbehind
#print(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', msg)) - tras todos os offline