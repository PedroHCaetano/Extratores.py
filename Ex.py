url = "https://www.alura.com.br/curso?curso=python"
print(url)

# Separa base e os parametros

indice_curso = url.find("curso")
indice_valor = indice_curso + len("curso") + 1
valor = url[indice_valor:]
print(valor)
