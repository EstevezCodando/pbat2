def longest_common_subsequence(s1: str, s2: str) -> (int, str):
    """
    Retorna o comprimento e a própria sequência comum mais longa (LCS) entre duas strings.

    :param s1: Primeira string.
    :param s2: Segunda string.
    :return: Uma tupla (comprimento_da_LCS, LCS).
    """
    # Comprimento das duas strings
    m, n = len(s1), len(s2)
    
    # Criação da matriz DP (m+1) x (n+1) para armazenar os comprimentos da LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Preenchimento da matriz dp com base no subproblema:
    # dp[i][j] representa o comprimento da LCS entre s1[:i] e s2[:j].
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstrução da LCS a partir da matriz dp
    lcs_length = dp[m][n]
    lcs_str = []

    # Partindo do fim (m, n) em direção ao início (0, 0)
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            # Caractere comum faz parte da LCS
            lcs_str.append(s1[i - 1])
            i -= 1
            j -= 1
        else:
            # Move-se na direção do valor maior entre dp[i-1][j] e dp[i][j-1]
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    # A LCS foi construída de trás para frente, então é preciso reverter
    lcs_str.reverse()
    
    return lcs_length, "".join(lcs_str)


def main() -> None:
    """
    Função principal para demonstrar o uso do longest_common_subsequence.
    """
    s1 = "ABCBDAB"
    s2 = "BDCABA"
    
    length, sequence = longest_common_subsequence(s1, s2)
    print(f"Strings: s1 = '{s1}', s2 = '{s2}'")
    print(f"Comprimento da LCS: {length}")
    print(f"LCS: '{sequence}'")


if __name__ == "__main__":
    main()
