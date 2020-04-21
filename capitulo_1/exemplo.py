# Problema:
# Voce nao tem uma tupla ou sequencia de N elementos que gostaria de desempacotar em uma colecao de N variaveis.
p = (4, 5)
x, y = p


# Solucao: qualquer sequencia(ou iteravel) pode ser desempacotada em variaveis por meio de uma operacao simples de atribuicao.
# O único requisito é que a quantidade de variaveis e a estrutura correspondam à sequencua.
#
data = ['ACME', 50, 91.1, (2012, 12, 20)]
name, shares, prices, date = data
