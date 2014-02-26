#useful math functions
def fibonacci_gen():
    a, b = 1, 0
    while True:
        yield a
        b += a
        yield b
        a += b
        
def get_nth_fibonacci(n):
    if not float(n).is_integer() or n < 1:
        raise ValueError
    root5 = pow(5, 0.5)
    ratio = (1 + root5) / 2
    return round((pow(ratio, n) - pow(1 - ratio, n)) / root5)

def factorial(x):
    if not float(x).is_integer() or x < 0:
        raise ValueError
    elif x < 2:
        return 1
    else:
        return x * factorial(x - 1)	

def GCF(x, y):
    if (y > x):  #swap the numbers
        x, y = y, x 
    remainder = x % y
    if (remainder == 0):
        return y
    else:
        return GCF(y, remainder)

def LCM(x, y):
    return int(x * y / GCF(x, y))

def PHI(): #golden ratio    
    return (1 + pow(5, 0.5)) / 2
    
def is_prime(x):
    if x < 0 or not float(x).is_integer():
        raise ValueError
    if x < 2:
        return False
    for i in range(2, int(pow(x, 0.5)) + 1):
        if x % i == 0:
            return False        
    return True    

def is_palindrome(x):
    return str(x) == str(x)[::-1]

def reduce_fraction(numerator, denominator):
    gcf = GCF(numerator, denominator)
    numerator = numerator / gcf
    denominator = denominator / gcf
    return numerator, denominator