import time
from typing import Dict

def fibonacci_recursive(n: int) -> int:
    """
    Retorna o n-ésimo número da sequência de Fibonacci de forma recursiva, sem otimização.

    :param n: Índice da sequência de Fibonacci (0-based).
    :return: n-ésimo número da sequência.
    :raises ValueError: Se n for negativo.
    """
    if n < 0:
        raise ValueError("O índice não pode ser negativo.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memoized(n: int, memo: Dict[int, int] = None) -> int:
    """
    Retorna o n-ésimo número da sequência de Fibonacci de forma recursiva, 
    utilizando memoização para otimizar o cálculo.

    :param n: Índice da sequência de Fibonacci (0-based).
    :param memo: Dicionário usado como cache (chave = índice, valor = Fibonacci).
    :return: n-ésimo número da sequência.
    :raises ValueError: Se n for negativo.
    """
    if n < 0:
        raise ValueError("O índice não pode ser negativo.")
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


def main():
    """
    Função principal para demonstrar e comparar o tempo de execução
    das implementações recursiva simples e recursiva com memoização.
    """
    valores_de_teste = [10, 20, 30, 35]

    print("### Fibonacci Recursivo (Sem Memoização) ###")
    for valor in valores_de_teste:
        inicio = time.time()
        resultado = fibonacci_recursive(valor)
        fim = time.time()
        print(f"Fib({valor}) = {resultado} | Tempo: {fim - inicio:.6f} s")

    print("\n### Fibonacci Recursivo (Com Memoização) ###")
    for valor in valores_de_teste:
        inicio = time.time()
        resultado = fibonacci_memoized(valor)
        fim = time.time()
        print(f"Fib({valor}) = {resultado} | Tempo: {fim - inicio:.6f} s")


if __name__ == "__main__":
    main()
