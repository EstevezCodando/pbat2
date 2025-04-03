import random

def partition(arr, low, high):
    """
    Função de partição (usada no QuickSort e QuickSelect).
    Escolhe o pivô como o último elemento do subarray [low..high].
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    """
    Retorna o k-ésimo menor elemento do subarray arr[low..high].
    k é 1-based (1 <= k <= len(subarray)).
    """
    if low <= high:
        pivot_index = partition(arr, low, high)
        
        # Tamanho do subarray 'à esquerda + pivô'
        left_size = pivot_index - low + 1
        
        if left_size == k:
            return arr[pivot_index]
        elif left_size > k:
            return quickselect(arr, low, pivot_index - 1, k)
        else:
            return quickselect(arr, pivot_index + 1, high, k - left_size)
    
    return None
def median_quickselect(arr):
    """
    Retorna a mediana da lista arr.
    - Se n for ímpar, retorna o elemento do meio.
    - Se n for par, retorna a média dos dois elementos centrais.
    """
    n = len(arr)
    if n == 0:
        return None

    # Para não alterar a lista original:
    temp = arr[:]
    
    if n % 2 == 1:
        # Ímpar: mediana é o elemento no índice (n//2) (0-based)
        # Mas quickselect usa k 1-based:
        k = (n + 1) // 2  
        return quickselect(temp, 0, n - 1, k)
    else:
        # Par: média dos dois valores centrais
        k1 = n // 2         # ex: se n=6, k1=3
        k2 = k1 + 1         # ex: k2=4
        val1 = quickselect(temp, 0, n - 1, k1)
        val2 = quickselect(temp, 0, n - 1, k2)
        return (val1 + val2) / 2

def quickselect_k_smallest(arr, k):
    """
    Retorna os k menores elementos de arr sem ordená-la completamente.
    Os elementos resultantes não estarão, necessariamente, em ordem crescente,
    mas serão os k menores.
    """
    n = len(arr)
    if k <= 0 or k > n:
        return []

    # Cria cópia para não alterar a lista original
    temp = arr[:]

    # Usamos QuickSelect para colocar o k-ésimo menor na posição (k-1)
    quickselect(temp, 0, n - 1, k)

    # Agora, os k menores elementos estão nas primeiras k posições,
    # embora não estejam necessariamente ordenados.
    return temp[:k]

def quickselect_k_smallest_sorted(arr, k):
    """
    Retorna os k menores elementos de arr em ordem crescente.
    """
    subset = quickselect_k_smallest(arr, k)
    return sorted(subset)
