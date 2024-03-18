url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real "
#url = "    "
print(url)

# Sanitização da URL
url = url.strip()

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia!")


# Separa a base e os parametros
indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao] #Antes do : tem um zero (0) e funciona sem ele.
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de um parametro
parametro_busca = "moedaOrigem"
indice_parametro = url_parametros.find(parametro_busca)
#print(indice_parametro) #19 é o M de moedaOrigem
indice_valor = indice_parametro + len(parametro_busca) + 1
#print(indice_valor) #31 é o R de Real
indice_e_comercial = url_parametros.find("&", indice_valor)
if indice_parametro == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor) # indice_valor = R e : entrega os valores 32, 33, 34
