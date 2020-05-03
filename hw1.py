'''
Homework due January 28, 2019
@author: Lindsay Maggioncalda; lnm22
'''

# import only standard Python 3 libraries here.
import math


# input: positive integer x
# output: True or False
def isPrime(x):
    # 0 and 1 are not considered prime
    if x == 1 or x == 0: 
        return False
    
    # find square root of x
    # only look for factors less than or equal to sqrt x
    sqrtx = math.floor(math.sqrt(x))
    for num in range(sqrtx+1):
        if num > 1:
            # print(num)
            if x%num == 0:
                # number is non-prime
                return False
    return True
    

# input: positive integer x
# output: True or False
def isDivBySeven(x):
    print(x) # do not remove this line
    if x < 10:
        if x%7 == 0:
            return True
        else: 
            return False
    else:
        length = len(str(x))
        # print("length is ",length)
        b = str(x)[-1]
        # print("b is "+b)
        a = str(x)[0:length-1]
        # print("a is "+a)
        y = abs(int(a) - 2 * int(b))
        return isDivBySeven(y)


if __name__ == '__main__':
    print(isDivBySeven(1234))