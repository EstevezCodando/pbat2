def factorial(n: int) -> int:
    """
    Calcula o fatorial de um número inteiro positivo usando recursão.

    :param n: Número inteiro para o qual se deseja calcular o fatorial.
              É esperado que n seja >= 0.
    :return: O valor de n! (fatorial de n).
    :raises ValueError: Se n for negativo.
    """
    if n < 0:
        raise ValueError("O número não pode ser negativo.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def main() -> None:
    """
    Função principal para demonstrar o uso da função factorial.
    """
    valores_de_teste = [0, 1, 5, 7, 10]
    for valor in valores_de_teste:
        try:
            resultado = factorial(valor)
            print(f"Fatorial de {valor} = {resultado}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
