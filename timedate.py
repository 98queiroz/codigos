import requests
from datetime import datetime
from prompt_toolkit.validation import Validator, ValidationError

#vairavel global
timezones = []

def hora(timezone):
    url = 'https://worldtimeapi.org/api/timezone/' + timezone

    resposta = requests.get(url)

    hora = datetime.fromisoformat(resposta.json()['datetime'])

    return hora


def timezones_disponiveis():
    global timezones

    if (len(timezones) > 0):
        return timezones

    url = 'https://worldtimeapi.org/api/timezone/'
    resposta = requests.get(url)
    timezones = resposta.json()

    return timezones
    
class TimezoneValidador(Validator):
    def validate(self,document):
        texto = document.text

        if texto not in timezones_disponiveis():
            raise ValidationError(message='Timezone não disponivel: ' + texto)