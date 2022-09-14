from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays
from calendar import monthrange

setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
#%A - nome do dia, %d -numero do dia do mes %B - nome do mes %Y - ano com 4 digitos
formatacao = dt.strftime('%A, %d de %B de %Y')
#formatação para dia, mes, ano - hora, minuto, segundo
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
#print(formatacao)
#print(mes_atual, mdays[mes_atual])

#ultimo dia do mes em ano bissexto

print(monthrange(2022,8))

dia_semana, ultimo_dia = monthrange(2022,8)
print(ultimo_dia)

ultimos_dias_de_meses_do_ano_atual = [
    monthrange(datetime.now().year, mes)[1] for mes in range(1,13)
    ]
print(ultimos_dias_de_meses_do_ano_atual)