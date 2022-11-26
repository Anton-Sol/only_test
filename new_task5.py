import math
import itertools
import sympy

'''
def is_prime(x:int):
    if x%2 == 0:
        return x == 2
    for i in range(3, math.ceil(x**0.5), 2):
        if x%i == 0:
            return False
    return True
'''
def main():
    for i in (7,4):
        for j in itertools.permutations( map( str, list( range(i, 0 ,-1) ) ) ) :
            x = int(''.join(j))
            if sympy.prime(x):
                print(x)
                return


main()

'''odsfvdafsasfasd'''