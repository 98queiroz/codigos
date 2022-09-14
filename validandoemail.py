import re

emails = """
Valid email addresses
o-que_vai.te+dar+dor-de.cabeca@gmail-com-traco.com.br
simple@example.com
very.common@example.com
disposable.style.email.with+symbol@example.com
other.email-with-hyphen@example.com
fully-qualified-domain@example.com
user.name+tag+sorting@example.com
x@example.com
example-indeed@strange-example.com
example@s.example
a@a.com.br
mailhost!username@example.org
user%example.com@example.org
email@example.com
firstname.lastname@example.com
email@subdomain.example.com
firstname+lastname@example.com
email@123.123.123.123
"email"@example.com
1234567890@example.com
email@example-one.com
_______@example.com
email@example.name
email@example.museum
email@example.co.jp
firstname-lastname@example.com


Invalid email addresses
Abc.example.com
<aqui-te-um@email-pra-validar.com.br>
A@b@c@example.com
a"b(c)d,e:f;g<h>i[j\k]l@example.com
just"not"right@example.com
this is"not\allowed@example.com
this\ still\"not\\allowed@example.com
plainaddress
#@%^%#$@#$@#.com
@example.com
<email@example.com>
email.example.com
email@example@example.com
.email@example.com
email.@example.com
email..email@example.com
あいうえお@example.com
email@example
email@-example.com
email@example..com
Abc..123@example.com
”(),:;<>[\]@example.com
just”not”right@example.com
this\ is"really"not\allowed@example.com
"""

#print(re.findall('^\w+(?:[.\-+!%l]\w+)*@\w+(?:[.\-]\w+)+$', emails,flags=re.MULTILINE))

print(re.findall('^[^\s<>\(\)[\]\.]+(?:\.[^\s<>\(\)\[\]\.]+)*@\w(?:[\.\-_]\w+)*$', emails, flags=re.M))
