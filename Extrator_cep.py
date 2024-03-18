endereco = "Rua Aimorés 21, Predio 2, Centro, Belo Horizonte, MG, 30140-073"

import re #Regular expression == RegEx

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
#? serve para colocar o [-] como opcional (pode ter ou não)
#[0-9] é de 0 a 9 || {5} é qnts vezes ele aparece
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)