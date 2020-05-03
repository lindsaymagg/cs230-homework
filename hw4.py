# import only standard Python 3 modules here

# AUTHOR = LINDSAY MAGGIONCALDA

'''
INSTRUCTIONS.
========================================================
For each for the following six functions, the input
consists of a set, A, and a relation R on set A. Function
"isPropertyX(A,R)" returns True if R has property X, and
False otherwise. You can assume A is a finite list of ints,
e.g. [1,3,5,7,9], and R is valid relation on A, e.g. [(1,3),
(3,1),(3,7)].
========================================================
'''

def isReflexive(A, R):
    # is reflexive if for every el a in A, there exists (a,a) in R
    for el in A:
        if ((el,el) not in R):
            return False
    return True
    
    
def isIrreflexive(A, R):
    for el in A:
        if ((el,el) in R):
            return False
    return True
        

def isTransitive(A, R):
    for el in R:
        a = el[0]
        b = el[1]
        for tup in R:
            if (tup[0] == b):
                c = tup[1]
                if ((a,c) not in R):
                    return False
    return True
    

def isAntisymmetric(A, R):
    for el in R:
        a = el[0]
        b = el[1]
        if (a != b):
            if ((b,a) in R):
                return False
    return True
        

def isSymmetric(A, R):
    for el in R:
        a = el[0]
        b = el[1]
        for tup in R:
            if ((b,a) not in R):
                return False
    return True

def isAsymmetric(A, R):
    for el in R:
        a = el[0]
        b = el[1]
        for tup in R:
            if ((b,a) in R):
                return False
    return True
    
if __name__ == '__main__': 
    set = [0, 1, 2]
    relation = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    print(isReflexive(set,relation))
    print(isIrreflexive(set,relation))
    print(isTransitive(set,relation))
    print(isAntisymmetric(set,relation))
    print(isSymmetric(set,relation))
    print(isAsymmetric(set,relation))