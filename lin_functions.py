from .MatrixClass import MatrixDimensionError


def determinant(A):
    """

    :param M: Matrix object.
    :return: Determinant of given matrix.
    """

    from copy import deepcopy
    M = deepcopy(A)
    if M.rows != M.columns:
        raise MatrixDimensionError("You can calculate a determinant of a square matrix only")

    det = 1
    e = 1E-9
    n = M.rows
    for i in range(n):
        k = i
        for j in range(i + 1, n):
            if abs(M[j][i]) > abs(M[k][i]):
                k = j
        if abs(M[k][i]) < e:
            det = 0
            break

        M[i], M[k] = M[k], M[i]
        if i != k:
            det *= -1

        det *= M[i][i]
        for j in range(i + 1, n):
            M[i][j] /= M[i][i]
        for j in range(n):
            if j != i and abs(M[j][i]) > e:
                for k in range(i + 1, n):
                    M[j][k] -= M[i][k] * M[j][i]

    return det
