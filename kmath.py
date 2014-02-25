#useful math functions
def fibonacci_gen():
    a, b = 1, 0
    while True:
        yield a
        b += a
        yield b
        a += b
        
def get_nth_fibonacci(n):
    root5 = pow(5, 0.5)
    ratio = (1 + root5) / 2
    return round((pow(ratio, n) - pow(1 - ratio, n)) / root5)

def E(): #base of natural logarithms
    return 2.71828183

def factorial(x):
    if x < 0:
        return None
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
    return 1.61803399	

def PI():  #returns pi
    return 3.14159265

def is_prime(x):
    #TODO
    pass    

def reduce_fraction(num, den):
    lcm = LCM(num, den)
    num = num / lcm
    den = num / lcm