def formatar_valor(valor):
    valor_str = str(valor)
    valor_formatado = ''
    if valor < 1000:
        valor_formatado = valor_str + ',00'
    elif valor < 10_000:
        valor_formatado = valor_str[0] + '.' + valor_str[1:] + ',00'
    elif valor < 100_000:
        valor_formatado = valor_str[:2] + '.' + valor_str[2:] + ',00'
    elif valor < 1_000_000:
        valor_formatado = valor_str[:3] + '.' + valor_str[3:] + ',00'
    return  valor_formatado

print(formatar_valor(500000))