# Short description:
# Usually, given two square matrices A and B it is not true that AB = BA.
# However, if B=cA, where c is a scalar, then AB=BA.

# *Expected outcome:* Implementation of an algorithm for testing experimentally such hypotheses.

# It is required to:

# 1. Take as input a integer N and a scalar c
# 2. Generate 10 random matrices N*N: A1, A2, …..A10
# 3. Generate 10 matrices as: B1=cA1, B2=cA2,....B10=cA10
# 4. Test the equality that Ai = Bi for i = 1, 2, 3, …., 10
# 5. Considering a number of threads T > 10, design a second version of the algorithm that uses multiprocessing to speedup the execution.
# 6. NB: as the number of threads is > 10, assigning each pair of matrices to a single process is not a valid solution, as some processes will be unused.

import numpy as np
import time

print("Demostration: given two square matrices A and B it is not true that AB = BA.\nHowever, if B=cA, where c is a scalar, then AB=BA.\n")
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('###################################')
print('CASE 1: B = c, where c is a scalar')
print('###################################')
print('Matrix A:')
print(A)
print('---')
B = 3
print('scalar Matrix B = 3')
print('---')

print('Matrix A multiplied by scalar Matrix B:')
print(np.dot(A,B))

print('---')
print('scalar Matrix B multiplied by Matrix A is the same as before:')
print(np.dot(B,A))
print('########################################')
print('CASE 2: B = c, where c is NOT a scalar')
print('########################################')
B= np.array([[7,6,7],[8,9,7],[10,11,10]])
print('Matrix B:')
print(B)
print('---')

print('Matrix A:')
print(A)

print('---')

print('Matrix A multiplied by Matrix B:')
print(np.dot(A,B))

print('---')

print('Matrix B multiplied by Matrix A:')
print(np.dot(B,A))

print('\nThis time the outcome is different!')
print('##############################################################')
print('End of demonstration. Beginning Algebraic Properties project.')
print('##############################################################')
print('Comparing A*c with c*A results, when c is or is NOT a scalar.\n')

# 1. Take as input a integer N and a scalar c
N = int(input("Define rows and columns of the square matrices:"))
c = int(input("Insert a scalar to be multiplied to matrix M:"))
#2. Generate 10 random matrices N*N: A1, A2, …..A10
# 3. Generate 10 matrices as: B1=cA1, B2=cA2,....B10=cA10

start = time.perf_counter()
for i in range(10):
    print(f'iteration number:{i}')
    M = np.random.randint(0, 5, size=(N, N))
    print(f"\nMatrix M{i}:\n{M}")
    cM = np.dot(c, M)
    #4. Test the equality that Ai = Bi for i = 1, 2, 3, …., 10
    print(f"\n c * M{i} :\n{cM}")
    print("\nAre the two arrays equal: \t", np.array_equal(M, cM), "!")
    print(f"cM{i} matrix is different from M{i}.")

    print(f"Let's check if cM{i} matrix is equal to Mc{i} (M{i}*c) matrix:\n")
    print(f"cM{i} matrix:\n{cM}\n")
    Mc = np.dot(M, c)
    print(f"Mc{i} matrix:\n{Mc}\n")

    try:
        np.array_equal(cM, Mc)
        print("\nAre the two arrays equal: \t", np.array_equal(cM, Mc), "!")
    except:
        raise Exception("Something went wrong, please try again")

finish = time.perf_counter()
print(f"It took {finish - start} second(s) to finish.")