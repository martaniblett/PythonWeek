def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

#import pytest
# import is_prime(or whatever file name where functions is) 

def test_is_prime():
    assert is_prime(3) == True
