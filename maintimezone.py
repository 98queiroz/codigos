from datetime import datetime
from timedate import TimezoneValidador, hora, timezones_disponiveis
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

#lista de timezone disponiveis
disponiveis = timezones_disponiveis()
#variavel que rece um completador de palavras passando a lista de timezones
#ignore case para ignora maiuscula e minuscula, e match middle, pra dar match no meio da palavra
opcoes_timezone = WordCompleter(disponiveis, ignore_case=True,match_middle=True)

#chamando o prompt, passando opcoes de time zone, validador(classe), e validador em tempo real
timezone = prompt('Escolha o timezone: ',completer = opcoes_timezone,
validator=TimezoneValidador(),validate_while_typing=False)
#print do resultado
print(timezone)

data_no_timezone = hora(timezone)
print(data_no_timezone.strftime("%d/%m/%Y %H:%M:%S"))