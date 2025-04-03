import numpy as np
import time
from gerar_vetor import gerar_vetor
from soma_openmp import soma_paralela

def soma_sequencial(vetor):
    return np.sum(vetor)

if __name__ == "__main__":
    vetor = gerar_vetor()

    # Tempo da soma sequencial
    inicio = time.time()
    resultado_seq = soma_sequencial(vetor)
    tempo_seq = time.time() - inicio
    print(f"Soma Sequencial: {resultado_seq:.2f} - Tempo: {tempo_seq:.6f} s")

    # Tempo da soma paralela (Cython + OpenMP)
    inicio = time.time()
    resultado_paralelo = soma_paralela(vetor)
    tempo_paralelo = time.time() - inicio
    print(f"Soma Paralela: {resultado_paralelo:.2f} - Tempo: {tempo_paralelo:.6f} s")

    print(f"Aceleração: {tempo_seq / tempo_paralelo:.2f}x mais rápido")
