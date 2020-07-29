######################################################
# Transverse-field Ising model Hamiltonian generator #
# (Periodic boundary condition)                      #
# Isaac H. Kim and Junyu Liu                         #
# MIT License                                        #
# 2020/7/29                                          #
######################################################
import numpy as np

X = np.array([[0, 1], [1, 0]])
Z = np.array([[1, 0], [0, -1]])
I = np.array([[1, 0], [0, 1]])


# Transverse field
def tf(l):
    """
    Args:
        l(int): Length of the chain

    Returns:
        np.ndarray: Sum of the transverse-field terms,
                    with unit coupling, in dense matrix
                    form.
    """
    out = np.zeros([2**l, 2**l])
    for i in range(l):
        out += np.kron(np.kron(np.eye(2**i), X),
                       np.eye(2**(l-i-1)))

    return out

# Ferromagnetic interaction
def ferro(l):
    """
    Args:
        l(int): Length of the chain

    Returns:
        np.ndarray: Sum of the ferromagnetic interaction
                    terms with unit coupling, in dense
                    matrix form.
    """
    out = np.zeros([2**l, 2**l])
    for i in range(l-1):
        out += np.kron(np.kron(np.eye(2**i), np.kron(Z, Z)),
                       np.eye(2**(l-i-2)))

    out += np.kron(np.kron(Z, np.eye(2**(l-2))), Z)

    return out
                

# Ising Hamiltonian generator
def isingHam(l, J, h):
    """
    Args:
        l(int): Length of the chain
        J(float): Ferromagnetic interaction strength
        h(float): On-site magnetization strength

    Returns:
        np.ndarray: Ising Hamiltonian, in dense matrix
                    form.
    """
    return tf(l)*h + ferro(l)*J 
