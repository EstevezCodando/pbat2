import random
import time

def quicksort(arr, pivot_type='first'):
    """
    Ordena a lista arr usando QuickSort, com diferentes estratégias de pivô:
      - 'first': primeiro elemento
      - 'last': último elemento
      - 'median': mediana de três (primeiro, meio, último)
    Retorna uma nova lista ordenada.
    """

    # Se a lista tiver 0 ou 1 elemento, já está ordenada
    if len(arr) <= 1:
        return arr

    # Escolhe o pivô de acordo com pivot_type
    if pivot_type == 'first':
        pivot = arr[0]
    elif pivot_type == 'last':
        pivot = arr[-1]
    elif pivot_type == 'median':
        first = arr[0]
        middle = arr[len(arr)//2]
        last = arr[-1]
        pivot = sorted([first, middle, last])[1]  # mediana de três
    else:
        raise ValueError("Tipo de pivô inválido. Use 'first', 'last' ou 'median'.")

    # Particionar a lista em relação ao pivô
    left = []
    right = []
    equal = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            equal.append(x)

    # Recursivamente ordena as partições e combina
    return quicksort(left, pivot_type) + equal + quicksort(right, pivot_type)

