def naive_multiplication(matrixA, matrixB):
    """
    matrixA: a m x n matrix
    matrixB: a n x r matrix
    """
    m = len(matrixA)
    n = len(matrixB)
    r = len(matrixB[0])

    if n != len(matrixA[0]):
        print("Either dimension of matrix A or B  is error.")
        return None
    else:

        result = []

        for row in range(m):
            rowOfMatrixA = matrixA[row]
            row_temp = []

            for col in range(r):
                row_temp.append(sum([rowOfMatrixA[i]*matrixB[i][col] for i in range(r)]))

            result.append(row_temp)

        return result
        
def concatenate(lu,ld,ru,rd):
    result = []
    row_u = len(lu)
    row_d = len(ld)

    for i in range(row_u):
        row_temp = lu[i] + ru[i]
        result.append(row_temp)

    for j in range(row_d):
        row_temp = ld[j] + rd[j]
        result.append(row_temp)

    return result

def partitoionMatrix(matrix, startRow, endRow, startCol, endCol):
    result = []

    for row in range(startRow, endRow + 1):
        row_temp = []

        for col in range(startCol, endCol + 1):
            row_temp.append(matrix[row - 1][col - 1])
        result.append(row_temp)
    return result


def matrixSubtraction(matrixA, matrixB, operator = "-"):

    result = []

    if operator == "-":
        operation = lambda x,y: x-y
    else:
        operation = lambda x,y: x+y

    for row in range(len(matrixA)):
        row_temp = []

        for col in range(len(matrixA[0])):
            row_temp.append(operation(matrixA[row][col],matrixB[row][col]))

        result.append(row_temp)

    return result

def strassen_algo(matrixA, matrixB):
    """
    matrixA: a m x n matrix
    matrixB: a n x r matrix
    """
    m = len(matrixA)
    n = len(matrixB)

    if m == 1: # trivial solution of recursion
        return [[matrixA[0][0]*matrixB[0][0]]]

    r = len(matrixB[0])

    if n != len(matrixA[0]):
        print("Either dimension of matrix A or B  is error.")
        return None

    else:
        halfLenOfRow, halfLenOfCol = int(m/2), int(n/2)

        a = partitoionMatrix(matrixA, 1, halfLenOfRow, 1, halfLenOfCol)
        b = partitoionMatrix(matrixA, 1, halfLenOfRow, halfLenOfCol + 1, n)
        c = partitoionMatrix(matrixA, halfLenOfRow + 1, m, 1, halfLenOfCol)
        d = partitoionMatrix(matrixA, halfLenOfRow + 1, m, halfLenOfCol + 1, n)
        e = partitoionMatrix(matrixB, 1, halfLenOfRow, 1, halfLenOfCol)
        f = partitoionMatrix(matrixB, 1, halfLenOfRow, halfLenOfCol + 1, n)
        g = partitoionMatrix(matrixB, halfLenOfRow + 1, m, 1, halfLenOfCol)
        h = partitoionMatrix(matrixB, halfLenOfRow + 1, m, halfLenOfCol + 1, n)
        
        p1 = strassen_algo(a, matrixSubtraction(f,h))
        p2 = strassen_algo(matrixSubtraction(a,b, "+"),h)
        p3 = strassen_algo(matrixSubtraction(c,d, "+"),e)
        p4 = strassen_algo(d, matrixSubtraction(g,e))
        p5 = strassen_algo(matrixSubtraction(a,d,"+"),matrixSubtraction(e,h,"+"))
        p6 = strassen_algo(matrixSubtraction(b,d),matrixSubtraction(g,h,"+"))
        p7 = strassen_algo(matrixSubtraction(a,c),matrixSubtraction(e,f,"+"))

        lu = matrixSubtraction(matrixSubtraction(p5,p4,"+"), matrixSubtraction(p6, p2),"+")
        ru = matrixSubtraction(p1, p2, "+")
        ld = matrixSubtraction(p3, p4, "+")
        rd = matrixSubtraction(matrixSubtraction(p1,p5,"+"), matrixSubtraction(p3, p7,"+"))

        result = concatenate(lu,ld,ru,rd)
    return result



if __name__ == "__main__":
    matrixA = [[1,2,5,5],
               [2,3,5,4],
               [4,6,5,1],
               [1,5,8,1]
              ]

    matrixB = [[1,2,0,105],
               [2,3,5,6],
               [5,6,4,9],
               [5,100,5,1020]
              ]
    a = [
         [1,2],
         [2,2]
               ]
    b = [
         [1,4],
         [7,5]
               ]
    for element in strassen_algo(matrixA, matrixB):
        print(element)

    print("\nCorrect\n")
    for element in naive_multiplication(matrixA, matrixB):
        print(element)

