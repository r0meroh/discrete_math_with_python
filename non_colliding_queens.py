# this excercise calculates how many queens on a given sized chessboard
# can exist at once without their paths causing a collision.

import itertools as itr

def is_solution(permutation):
    for(x1, x2) in itr.combinations(range(len(permutation)), 2):
        if abs(x1 - x2) == abs(permutation[x1] - permutation[x2]):
            return False
    return True

assert(is_solution([1,3,0,2]) == True)
print(is_solution([1,3,0,2]))
