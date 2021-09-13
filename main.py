import random

from heapsort import heapSort
from insercao import ordenacao_insercao
from mergesort import mergesort
from quicksort import quicksort
from selecao import ordenacao_selecao

# Define os vetores
A = random.sample(range(0, 20), 20)
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

# HeapSort - AINDA NÃO FUNCIONAM
print("Estado inicial dos vetores para HeapSort: ", D)
heapSort(D)
print('Fim do algoritmo de HeapSort:', D)
print('\n\n\n')

# E = [6, 8, 4, 1, 3, 2, 5, 0, 7, 9]

# QuickSort
print("Estado inicial dos vetores para QuickSort: ", E)
quicksort(E, 0, len(E) - 1 )
print('Fim do algoritmo de QuickSort:', E)
print('\n\n\n')