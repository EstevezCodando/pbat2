
import numpy as np

def gerar_vetor(tamanho=10000):
    return np.random.uniform(1, 100000, tamanho).astype(np.float64)

if __name__ == "__main__":
    vetor = gerar_vetor()
    print("Vetor gerado com sucesso!")
