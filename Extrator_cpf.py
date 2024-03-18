Pessoa = "Rafaela Brasil, CPF: 718.457.190-85"

import re

padrao = re.compile("[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}")
busca = padrao.search(Pessoa)

if busca:
    cpf = busca.group()
    print(cpf)
    
    
