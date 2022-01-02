Similaridade
============

Este projeto tem como objetivo auxiliar em situações em que são necessárias encontrar a similaridade (Em %) entre valores de string entre dois dataframes.

Para desenvolve-lo, utilizei uma base genérica com valores de municípios brasileiros não-estruturados e uma base retirada do IBGE com os nomes corretos destes municípios. Com as duas bases, comparo linha por linha procurando similaridades entre as duas. A função criada para fazer a busca aceita um valor *float*, que serve para definir a % de similaridade aceita para, na base genérica, retornar o valor (Na própria base) do município correto.
