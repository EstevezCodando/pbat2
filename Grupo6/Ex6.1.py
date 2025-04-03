from typing import List, Tuple

def knapsack_01(items: List[Tuple[int, int]], capacity: int) -> int:
    """
    Resolve o problema da mochila 0-1 usando programação dinâmica.

    :param items: Lista de tuplas (peso, valor).
    :param capacity: Capacidade máxima da mochila.
    :return: Valor máximo que pode ser alcançado respeitando a capacidade.
    """
    n = len(items)
    
    # dp[i][w] representará o valor máximo obtido usando até i itens 
    # (índices de 1 a i) com capacidade de w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        peso_item, valor_item = items[i - 1]
        for w in range(1, capacity + 1):
            if peso_item <= w:
                # Pode escolher entre não pegar o item (dp[i-1][w])
                # ou pegar o item (dp[i-1][w - peso_item] + valor_item)
                dp[i][w] = max(
                    dp[i - 1][w], 
                    dp[i - 1][w - peso_item] + valor_item
                )
            else:
                # Não é possível pegar este item
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]


def retrieve_items(items: List[Tuple[int, int]], capacity: int, dp: List[List[int]]) -> List[int]:
    """
    Reconstrói quais itens foram selecionados para atingir o valor máximo.
    
    :param items: Lista de tuplas (peso, valor).
    :param capacity: Capacidade usada durante a construção do dp.
    :param dp: Tabela dp preenchida pela função knapsack_01.
    :return: Lista de índices dos itens que foram selecionados.
    """
    n = len(items)
    selected_items = []
    
    # Percorre a matriz dp de trás para frente
    i, w = n, capacity
    while i > 0 and w >= 0:
        # Se o valor na linha atual difere da linha anterior,
        # significa que o item i-1 foi incluído.
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= items[i - 1][0]  # subtrai o peso do item
        i -= 1
    
    selected_items.reverse()  # A reconstrução é feita de trás pra frente
    return selected_items


def knapsack_01_with_items(items: List[Tuple[int, int]], capacity: int) -> Tuple[int, List[int]]:
    """
    Resolve o problema da mochila 0-1 usando programação dinâmica
    e retorna tanto o valor máximo quanto os itens escolhidos.
    
    :param items: Lista de tuplas (peso, valor).
    :param capacity: Capacidade máxima da mochila.
    :return: (valor_máximo, lista_de_indices_itens_selecionados)
    """
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Preenche a tabela dp
    for i in range(1, n + 1):
        peso_item, valor_item = items[i - 1]
        for w in range(1, capacity + 1):
            if peso_item <= w:
                dp[i][w] = max(
                    dp[i - 1][w], 
                    dp[i - 1][w - peso_item] + valor_item
                )
            else:
                dp[i][w] = dp[i - 1][w]
    
    valor_maximo = dp[n][capacity]
    itens_escolhidos = retrieve_items(items, capacity, dp)
    
    return valor_maximo, itens_escolhidos


def main():
    """
    Função principal para testar a implementação da Mochila 0-1.
    """
    # Exemplo 1
    items1 = [(2, 3), (3, 4), (4, 5), (5, 8)]
    capacity1 = 5
    valor_maximo1 = knapsack_01(items1, capacity1)
    print(f"[Exemplo 1] Valor máximo (sem reconstrução de itens): {valor_maximo1}")
    
    valor_maximo1_b, itens_escolhidos1 = knapsack_01_with_items(items1, capacity1)
    print(f"[Exemplo 1] Valor máximo: {valor_maximo1_b}")
    print(f"[Exemplo 1] Itens escolhidos (índices): {itens_escolhidos1}")
    print(f"[Exemplo 1] Detalhes dos itens escolhidos: {[items1[i] for i in itens_escolhidos1]}")
    print("---")
    
    # Exemplo 2
    items2 = [(1, 1), (3, 4), (4, 5), (5, 7)]
    capacity2 = 7
    valor_maximo2 = knapsack_01(items2, capacity2)
    print(f"[Exemplo 2] Valor máximo (sem reconstrução de itens): {valor_maximo2}")
    
    valor_maximo2_b, itens_escolhidos2 = knapsack_01_with_items(items2, capacity2)
    print(f"[Exemplo 2] Valor máximo: {valor_maximo2_b}")
    print(f"[Exemplo 2] Itens escolhidos (índices): {itens_escolhidos2}")
    print(f"[Exemplo 2] Detalhes dos itens escolhidos: {[items2[i] for i in itens_escolhidos2]}")
    print("---")
    
    # Exemplo 3
    items3 = [(2, 10), (2, 10), (4, 12), (6, 20), (3, 15)]
    capacity3 = 9
    valor_maximo3_b, itens_escolhidos3 = knapsack_01_with_items(items3, capacity3)
    print(f"[Exemplo 3] Valor máximo: {valor_maximo3_b}")
    print(f"[Exemplo 3] Itens escolhidos (índices): {itens_escolhidos3}")
    print(f"[Exemplo 3] Detalhes dos itens escolhidos: {[items3[i] for i in itens_escolhidos3]}")


if __name__ == "__main__":
    main()
