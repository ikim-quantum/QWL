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
        if s==0:
            out = np.kron(out, I)
        elif s==1:
            out = np.kron(out, X)
        elif s==2:
            out = np.kron(out, Y)
        else:
            out = np.kron(out, Z)

    return out
        

