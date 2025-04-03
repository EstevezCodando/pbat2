import random

def partition(arr, low, high):
    """
    Função de partição (usada no QuickSort e QuickSelect).
    Escolhe o pivô como o último elemento do subarray.
    """
    pivot = arr[high]
    i = low - 1  # índice para o menor elemento
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Coloca o pivô em sua posição final
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # índice do pivô corretamente posicionado



def quickselect(arr, low, high, k):
    """
    Retorna o k-ésimo menor elemento do subarray arr[low..high].
    """
    if low <= high:
        # Particiona o array
        pivot_index = partition(arr, low, high)

        # Quantidade de elementos à esquerda do pivô
        # (incluindo o pivô na contagem)
        left_size = pivot_index - low + 1

        if left_size == k:
            # O pivô está exatamente na posição do k-ésimo menor
            return arr[pivot_index]
        elif left_size > k:
            # k-ésimo menor está no lado esquerdo do pivô
            return quickselect(arr, low, pivot_index - 1, k)
        else:
            # k-ésimo menor está no lado direito; precisamos ajustar k
            return quickselect(arr, pivot_index + 1, high, k - left_size)

    # Caso de erro ou lista vazia
    return None

def find_kth_smallest(arr, k):
    """
    Encontra o k-ésimo menor elemento da lista arr,
    assumindo 1 <= k <= len(arr).
    """
    # Vamos criar uma cópia para não alterar a lista original
    arr_copy = arr[:]
    return quickselect(arr_copy, 0, len(arr_copy) - 1, k)
def test_quickselect():
    # Fixar seed para reprodutibilidade (opcional):
    # random.seed(42)

    NUM_LISTS = 10
    LIST_SIZE = 10000
    K_TESTS = 5

    for i in range(NUM_LISTS):
        # Gera lista com 10.000 números entre 1 e 1000
        arr = [random.randint(1, 1000) for _ in range(LIST_SIZE)]

        print(f"\n--- Lista {i+1} ---")

        # Para cada lista, escolhe 5 valores de k
        for _ in range(K_TESTS):
            k = random.randint(1, LIST_SIZE)
            
            kth_value = find_kth_smallest(arr, k)
            print(f"k = {k:5}, k-ésimo menor elemento = {kth_value}")

            # (Opcional) Verificar correção comparando com a lista ordenada
            # sorted_arr = sorted(arr)
            # assert sorted_arr[k-1] == kth_value, "Valor incorreto!"
            # ou podemos apenas imprimir
            # print(f"Verificado: {sorted_arr[k-1]} (esperado)")
