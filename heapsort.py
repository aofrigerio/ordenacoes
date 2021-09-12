def heapsort(A, n):
    # Primeiro estágio: construção do heap.
    for i in range(2, n):
        promove(A, i)

    # Segundo estágio: construção da sequência ordenada.
    for i in range(n, 1, -1):
        A[1], A[i] = A[i], A[1]
        demove(A, i - 1)

def promove(A, n):
    i = n
    print(A)
    while True:
        # Elemento chegou na raiz da árvore.
        if i == 1:
            break

        # Elemento chegou na posição correta.
        p = i // 2
        if A[p] >= A[i]:
            break

        # Troca elemento de lugar com o pai.
        A[p], A[i] = A[i], A[p]
        i = p


def demove(A, n):
    i = 1
    print(A)
    while True:
        c = 2 * i

        # Elemento não tem mais filhos.
        if c > n:
            break

        # Encontra o índice do maior dos filhos.
        if c + 1 <= n:
            if A[c + 1] > A[c]:
                c += 1

        # O elemento é menor que seu maior filho.
        if A[i] <= A[c]:
            break

        # Troca elemento de lugar com o maior filho.
        A[c], A[i] = A[i], A[c]
        i = c