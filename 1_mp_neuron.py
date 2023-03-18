# resources : https://towardsdatascience.com/mcculloch-pitts-model-5fdf65ac5dd1

import numpy as np
import itertools

def and_function(x):
    threshold = len(x[0])
    sum = 0
    result = []
    for i in x:
        sum = 0
        for j in i:
            sum += j
    
        if(sum >= threshold):
            result.append(1)
        else:
            result.append(0)
    
    return result


def or_function(x):
    threshold = 1
    sum = 0
    result = []
    for i in x:
        sum = 0
        for j in i:
            sum += j
    
        if(sum >= threshold):
            result.append(1)
        else:
            result.append(0)
    
    return result

def not_function(x):
    if x > 0:
        return 1
    else:
        return 0


def takeInputAndProcess():
    # print(all_permutations) -> list of tuples
    choice = int(input('Enter choice - \n 1-AND \n 2-OR \n 3-NOT \n'))

    if (choice == 1 or choice == 2):
        n = int(input('Enter n - '))
        all_permutations = list(itertools.product((0,1), repeat=n))

        if (choice == 1):
            print('    ', 'AND')
            result = and_function(all_permutations)
            for i in range(len(result)):
                print(all_permutations[i], '\t', result[i])
        else:
            print('    ', 'OR')
            result = or_function(all_permutations)
            for i in range(len(result)):
                print(all_permutations[i], '\t', result[i])
    else:
        n = int(input('Enter input for NOT neuron - '))
        print(n, '\t', not_function(n))

takeInputAndProcess()