import random

from insercao import ordenacao_insercao
from mergesort import mergesort
from selecao import ordenacao_selecao

# Define os vetores
A = random.sample(range(0, 10), 10)
B = A.copy()
C = A.copy()
D = A.copy()
E = A.copy()

# Inserção
print("Estado inicial dos vetores para inserção: ", A)
ordenacao_insercao(A)
print('Fim do algoritmo de inserção:', A)
print('\n\n\n')

# Ordenação
print("Estado inicial dos vetores para seleção: ", B)
ordenacao_selecao(B)
print('Fim do algoritmo de seleção:', B)
print('\n\n\n')


# Merge
print("Estado inicial dos vetores para Merge: ", C)
aux = [0] * len(C)
mergesort(C, aux, 0, len(C) - 1)
print('Fim do algoritmo de Merge:', C)
print('\n\n\n')