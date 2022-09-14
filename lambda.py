dicionario = {
    'marca':'mercedes',
    'modelo':'classe A',
    'ano':'2005'
}

ordenado = sorted(dicionario.items(),key=lambda item: item[1])
print(ordenado)