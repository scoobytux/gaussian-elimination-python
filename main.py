"""
    @Author: Le Nguyen Anh Tu
    @StudentID: 1751110
    @Email: tu.le_telecom@hcmut.edu.vn  
    @Date: 19/11/2021

    Linear Algebra Assignment (MT1007) - Semester 211

    Problem 3 source code
"""
import numpy as np
from helpers import *

def main():
    print('#-----------------------------------------------')
    print('#     LINEAR ALGEBRA (MT1007) - SEMESTER 211    |')
    print('#            ASSIGNMENT - PROBLEM 3             |')
    print('#-----------------------------------------------')
    n = int(input('Enter the number of Unknowns/Variables n: '))

    # Create an zero augmented matrix (A|b) 
    # sized n x (n + 1)
    augmented_matrix = np.zeros((n, n+1))


    
    """
        This part aims to enter entries of augmented matrix.
        Then, print the augmented matrix.
    """
    print('#-----------------------------------------------')
    print('Enter Entries of Augmented Matrix (A|b):\n')
    enterEntries(augmented_matrix, n)
    
    print("\nAugmented Matrix (A|b):\n")
    print(formatMatrix(augmented_matrix))
    
    

    """
        This part aims to use Gaussian Elimination/row reduction 
        algorithm for solving system of linear equations. 
    """
    print('#-----------------------------------------------')

    # Sort the initial augmented matrix and then print 
    # the sorted augmented matrix after sorting
    augmented_matrix, _ = sortRowsByNonZeroEntries(augmented_matrix)
    text = 'Firstly, Matrix\'s Row are sorted by number of\nNon-zero Entries\n'
    print(text + formatMatrix(augmented_matrix))

    # Apply Gaussian Elimination and print steps
    print("Apply Gaussian Elimination to matrix (A|b):\n")
    augmented_matrix = gaussianElimination(augmented_matrix, n)



    """
        This part aims to conclude the the solution of the 
        linear system. And then, in case of the system is
        consistent:
        - Find the exact solution if the system has unique 
          solution.
        - Find the number of free variables if the system has 
          infinitely many solutions.
    """
    print('#-----------------------------------------------')
    print('Conclude the Solution of the Linear System:\n')

    # Find coefficient matrix A by remove the last
    # column of augmented matrix (A|b)
    coefficient_matrix = augmented_matrix[:, :n]

    # Find rank(A) and rank(A|b)
    rank_A = np.linalg.matrix_rank(coefficient_matrix)
    rank_Ab = np.linalg.matrix_rank(augmented_matrix)

    # Conclude the solution of the linear system
    unique_sol = (rank_A == rank_Ab) and (rank_A == n)
    infinite_sol = (rank_A == rank_Ab) and (rank_A < n)
    no_sol = rank_A != rank_Ab

    text = '   rank(A) = rank(A|b) = {rank_Ab} '.format(rank_Ab=rank_Ab)
    if unique_sol: 
        text += '= n\n'
        text += '=> The system  has a unique solution'
        print(text)

        solve(augmented_matrix, n)

    if infinite_sol:
        text += '< n = {n}\n'.format(n=n)
        text += '=> The system  has infinite many solutions'
        print(text)

        findNumberOfFreeVar(n, rank_A)
    
    if no_sol:
        text = '   rank(A) = {rank_A} != rank(A|b) = {rank_Ab}\n'.format(rank_A=rank_A, rank_Ab=rank_Ab)
        text += '=> The system has no solution\n'
        print(text)


if __name__ == "__main__":
    main()