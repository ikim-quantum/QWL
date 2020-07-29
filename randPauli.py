##################################
# Random Pauli generator         #
# (Periodic boundary condition)  #
# Isaac H. Kim and Junyu Liu     #
# MIT License                    #
# 2020/7/29                      #
##################################
import numpy as np


I = np.array([[1, 0], [0, 1]])
X = np.array([[0, 1], [1, 0]])
Y = np.array([[0, -1j], [1j, 0]])
Z = np.array([[1, 0], [0, -1]])


def num2Pauli(i):
    if i==0:
        return I
    elif i==1:
        return X
    elif i==2:
        return Y
    elif i==3:
        return Z
    else:
        raise ValueError("Value must be 0, 1, 2, or 3.")


def randPauli(n):
    """
    Args:
        n(int): Number of qubits

    Returns:
        np.ndarray: Random Pauli over n qubits
    """
    seed = np.random.randint(low=0, high=4, size=n)

    out = np.eye(1)
    for s in seed:
        out = np.kron(out, num2Pauli(s))

    return out
        


#def applyRandPauli(psi):
#    """
#    Given a quantum state, applies a random Pauli directly
#    """
#    N, N_temp  = psi.size, psi.size
#    n = 0
#    while N_temp>0:
#        if N_temp%2==1:
#            raise ValueError("psi is not a power of 2.")
#        else:
#            N_temp //= 2
#            n += 1
#    seed = np.random.randint(low=0, high=4, size=n)

#    for i in range(n):
#        seed[i] = 
