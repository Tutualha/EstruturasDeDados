# Manipulando listas e dicionarios com a funcao sorted() e lambda
# lib para datas
from datetime import datetime

lista1 = [1, 3, 2, 4, 6, 8, 7, 9, 11, 13, 6.5, 10, 12.2, 13.4, 22, 21.5, 
          19, 30, 34, 314, 201, 321, 842, 1.2, 0,]

""" com a funcao sorted() podemos ordenar listas, tuplas e strings
 a funcao sorted() retorna uma nova lista ordenada, sem alterar a lista original
 daria pra fazer com sort() mas ela altera a lista original """

lista1_ord = sorted(lista1)

# Lista de dicionarios
lista2 = [{'nome': 'Joao M', 'idade': 19, 'data_nasc': '12/02/2006' },
          {'nome': 'Maria E', 'idade': 18, 'data_nasc': '01/03/2007' },
          {'nome': 'Davi L', 'idade': 23, 'data_nasc': '27/01/2002' },
          {'nome': 'Matheus', 'idade': 25, 'data_nasc': '10/05/2000' },
          {'nome': 'Richard E', 'idade': 19, 'data_nasc': '09/12/2006' },
          {'nome': 'Zoan', 'idade': 15, 'data_nasc': '10/04/2010' },
          {'nome': 'Dylan', 'idade': 24, 'data_nasc': '12/02/2001' },
          {'nome': 'Ronaldo', 'idade': 20, 'data_nasc': '12/02/2005' },
          {'nome': 'Rogerio', 'idade': 17, 'data_nasc': '12/02/2008' },]

# Funcao para vc conseguir ordenar a lista com 'data_nasc' no formato 'dd/mm/aaaa'
# pois o python nao ordena o formato 'dd/mm/aaaa' corretamente.
def data_nasc_br(data):
    dt = data.split('/')
    return datetime(
        # index 0 = dia, 1 = mes, 2 = ano
        int(dt[2]), int(dt[1]), int(dt[0])
    )

# Funcao para ordenar a lista de acordo com o valor que vc quer
def ordena_lista(valor):
    print(f'Os valores que estão sendo verificados: {valor["data_nasc"]}.')
    return data_nasc_br(valor['data_nasc'])
    # return valor['nome']

# opção sem def: lista2.sort(key=lambda x: x['nome'])
# ja essa deixa a lista original intacta e retorna uma nova lista ordenada
lista2_ord = sorted(lista2, key=ordena_lista)

print("\nOrdem Correta dos dados:\n", lista2_ord)

print("="*100)

print("\nLista 1 ordenada:", lista1_ord)
