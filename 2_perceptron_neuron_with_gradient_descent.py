# resources : Deep learning Nptel CS7015 lecture 2.5 Perceptron Learning Algorithm

import numpy as np
import random
import itertools

def perceptron_algo(all_permutation, w, bias, P, N, n):
    ''' all_permutation is array of training points (Xi's)
        w is weight matrix
        bias is y-intercept of line
        P is np array having all positive class data points
        N is np array having all negative class data points
        n is total number of data points
    '''
    print(w)
    while True:
        index = random.randint(0, 2 ** n - 1)
        x = all_permutation[index]

        prev_weights = w

        if (x in P) and (np.dot(x, w) + bias < 0):
            w = w + x
            bias = bias + 1

        elif (x in N) and (np.dot(x, w) + bias >= 0):
            w = w - x
            bias = bias - 1
        
        print(w)

        if ( (prev_weights == w).all() ):
            break
        

def takeInputAndProcess():
    choice = int(input('Enter choice - \n 1-AND \n 2-OR \n'))
    n = int(input('Enter n - '))
    all_permutations = list(itertools.product((0,1), repeat=n))
    all_permutations = np.array(all_permutations)
    bias = -n

    if (choice == 1):
        and_output = [0] * (2 ** n - 1)
        and_output.append(1)
        and_output = np.array(and_output)

        P = all_permutations[and_output == 1]
        N = all_permutations[and_output == 0]

        w = [0] * (n)
        w = np.array(w)

        perceptron_algo(all_permutations, w, bias, P, N, n)

    else:
        or_output = [1] * (2 ** n - 1)
        or_output.insert(0, 0)
        or_output = np.array(or_output)
        # print(or_output)
        P = all_permutations[or_output == 1]
        N = all_permutations[or_output == 0]

        w = [0] * (n)
        w = np.array(w)

        perceptron_algo(all_permutations, w, bias, P, N, n)


takeInputAndProcess()