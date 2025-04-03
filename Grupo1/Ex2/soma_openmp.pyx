# soma_openmp.pyx
from cython.parallel import prange
import numpy as np
cimport numpy as cnp
from libc.stdlib cimport malloc, free
from libc.stdio cimport printf

# Definição da função paralela
cdef double soma_paralela(double[:] vetor) nogil:
    cdef int i, n = vetor.shape[0]
    cdef double soma = 0.0

    # Loop paralelo usando OpenMP
    for i in prange(n, nogil=True):
        soma += vetor[i]

    return soma
