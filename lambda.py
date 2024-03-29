from __future__ import print_function
from fractions import Fraction

def product(fracs):
    # return fracs
    #lambda requires two arguements and it can only perform one function
    t = reduce(lambda x,y: x*y,fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(input()):
        fracs.append(Fraction(*map(int, raw_input().split())))
    result = product(fracs)
    print(*result)
