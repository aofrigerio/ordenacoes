def particao(A, inicio, fim):
    pivot = A[inicio]
    low = inicio + 1
    high = fim

    while True:
        print(A)
        while low <= high and A[high] >= pivot:
            high = high - 1

        while low <= high and A[low] <= pivot:
            low = low + 1

        if low <= high:
            A[low], A[high] = A[high], A[low]
        else:
            break

    A[inicio], A[high] = A[high], A[inicio]

    return high

def quicksort(array, start, end):
    if start >= end:
        return

    p = particao(array, start, end)
    quicksort(array, start, p-1)