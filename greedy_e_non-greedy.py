#metacaracteres: ^$()
# * -> 0 ou N 
# + -> 1 ou N
# ? -> 0 ou 1

import re

texto = '''
<p>Frase 1 </p> <p>Frase 2 </p><p>Frase 3 </p> <div>Frase 4 </div>

'''

print(re.findall(r'<[dpiv]{1,3}>', texto))