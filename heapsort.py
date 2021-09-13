def heapify(A, n, i):
    print(A)
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and A[i] < A[l]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and A[largest] < A[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        A[i], A[largest] = A[largest], A[i]  # swap

        # Heapify the root.
        heapify(A, n, largest)

    # The main function to sort an array of given size


def heapSort(A):
    n = len(A)

    for i in range(n, -1, -1):
        heapify(A, n, i)


    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]  # swap
        heapify(A, i, 0)