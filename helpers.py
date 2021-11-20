import numpy as np

def enterEntries(mat, n):    
    for row in range(n):
        for col in range(n+1):
            mat[row][col] = float(input(' (A|b)[{row}][{col}] = '.format(row=row, col=col)))
            


def formatMatrix(mat):
    text = ' ' + str(mat.round(2))[1:-2]
    rows = text.rsplit(']\n')

    minBlankPos = rows[0].rstrip().rfind(' ')
    for row in rows:
        pos = row.rstrip().rfind(' ')
        if pos != -1 and minBlankPos > pos:
            minBlankPos = pos
            
    for i in range(len(rows)):
        row_in_matrix_A = rows[i][:minBlankPos+1]
        row_in_matrix_A += '|'
        rows[i] = row_in_matrix_A + rows[i][minBlankPos+1:] + ']\n'

    return ''.join(rows)



def sortRowsByNonZeroEntries(mat):

    """
        Ex:
            [0 1 1 1]              [1 0 2 3]
            [1 0 2 3]      -->     [0 1 1 1]
            [0 0 0 5]              [0 0 9 1]
            [0 0 9 1]              [0 0 0 5]
    """
    sorted_mat = mat[(mat==0).sum(axis=1).argsort()]

    return sorted_mat, (mat==sorted_mat).all()



def gaussianElimination(mat, n):
    for row in range(n):
        for col in range(n+1):
            pivot = mat[row][col]
            if pivot == 0:
                continue
            
            if (row + 1 >= n) or (mat[row+1][col] == 0):
                break

            for next_row in range(row+1, n):
                if mat[next_row][col] == 0:
                    break;

                ratio = mat[next_row][col] / pivot
         
                for k in range(col, n+1):
                    mat[next_row][k] = mat[next_row][k] - ratio * mat[row][k]

                print(formatMatrix(mat))
            
            mat, equal = sortRowsByNonZeroEntries(mat)
            if not equal:
                 print(formatMatrix(mat))

            break

    return mat



def solve(mat, n):
    x = np.zeros(n)

    x[n-1] = mat[n-1][n] / mat[n-1][n-1]
 
    for i in range(n-2,-1,-1):
        x[i] = mat[i][n]
     
        for j in range(i+1,n):
            x[i] = x[i] - mat[i][j] * x[j]
     
        x[i] = x[i] / mat[i][i]
 
    print('\n   The solution is: ')
    for i in range(n):
        print('X%d = %0.2f' %(i,x[i]), end = '\t')
    print()



def findNumberOfFreeVar(n, rank_A):
        text = '\n   The number of free variables:\n'
        text += '=> n - rank(A) = {n} - {rank_A} = {result}\n'.format(n=n, rank_A=rank_A, result=n-rank_A)
        print(text)