#*** Parallel implementation ***
# Project name: Algebraic Properties
# Contact : mirco.macchi@live.it

import numpy as np
import time
from multiprocessing import Process
import os

start = time.perf_counter()
def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

# function with task of child processes
def multi_matrix(i,N,c):
    print(f'iteration number:{i}\n')
    info('main line')
    # 2. Generate 10 random matrices N*N: A1, A2, …..A10
    M = np.random.randint(0, 5, size=(N, N))
    print(f"\nMatrix M{i}:\n{M}")
    cM = np.dot(c, M)
    # 3. Generate 10 matrices as: B1=cA1, B2=cA2,....B10=cA10
    print(f"\n c * M{i} :\n{cM}")
    # 4. Test the equality that Ai = Bi for i = 1, 2, 3, …., 10
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
    print(f'done with iteration {i}')


if __name__ == '__main__':
    process_list = []
    num_processes = 10
    # 1. Take as input a integer N and a scalar c
    N = int(input("Define rows and columns of the square matrices:"))
    c = int(input("Insert a scalar to be multiplied to matrix M:"))

    for i in range(num_processes):

        # create processes
        p = Process(target=multi_matrix, args=(i,N,c ))

        # start the processes
        p.start()
        process_list.append(p)

    # wait until the processes have finished
    for process in process_list:
        # print info
        process.join()
    finish = time.perf_counter()
    print(f'Finished in {finish - start} second(s)')
