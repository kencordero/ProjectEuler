import math
import re
#useful math functions

PHI = (1 + pow(5, 0.5)) / 2

def factorial(x):
    if not float(x).is_integer() or x < 0:
        raise ValueError
    return 1 if x < 2 else x * factorial(x - 1)	
    
def fibonacci_gen():
    a, b = 1, 0
    while True:
        yield a
        b += a
        yield b
        a += b

def GCF(x, y):
    if (y > x):  #swap the numbers
        x, y = y, x 
    remainder = x % y
    return y if remainder == 0 else GCF(y, remainder)
    
def get_largest_prime_factor(x):
    lpf = 0 #largest prime factor
    i = 2
    while i <= x:
        while x % i == 0:
            x /= i
            lpf = i
        i += 1
    return lpf
    
def get_n_digits(x): # doesn't handle non-integers
    if x == 0:
        return 1
    return int(math.log10(abs(x))) + 1
    
def get_nth_fibonacci(n):
    if not float(n).is_integer() or n < 1:
        raise ValueError
    root5 = pow(5, 0.5)
    ratio = (1 + root5) / 2
    return round((pow(ratio, n) - pow(1 - ratio, n)) / root5)
    
def get_nth_prime(n):
    if not float(n).is_integer() or n < 1:
        raise ValueError
    if n == 1: return 2
    prime_counter = 1
    prime_candidate = 3 
    while prime_counter < n:
        factor_candidate = 3
        prime_candidate_root = math.sqrt(prime_candidate)
        while factor_candidate <= prime_candidate_root:
            if prime_candidate % factor_candidate == 0: break
            factor_candidate += 2
        if factor_candidate > prime_candidate_root: prime_counter += 1
        prime_candidate += 2
    return prime_candidate - 2

def get_smallest_prime_factor(x):
    i = 2
    while i <= x:
        if x % i == 0:
            return i
        i += 1

def is_palindrome(x):
    return str(x) == str(x)[::-1]
    
def is_phone_number(x):
    phone_pattern = (r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''')
    return re.search(phone_pattern, x, re.VERBOSE)

def is_prime(x):
    if x < 0 or not float(x).is_integer():
        raise ValueError
    if x < 2:
        return False
    for i in range(2, int(pow(x, 0.5)) + 1):
        if x % i == 0:
            return False        
    return True
    
def is_roman(x):
    pattern = '''
        ^                   # beginning of string
        M{0,3}              # thousands - 0 to 3 Ms
        (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                            #            or 500-800 (D, followed by 0 to 3 Cs)
        (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                            #        or 50-80 (L, followed by 0 to 3 Xs)
        (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                            #        or 5-8 (V, followed by 0 to 3 Is)
        $                   # end of string
        '''
    return re.search(pattern, x, re.VERBOSE)

def LCM(x, y):
    return int(x * y / GCF(x, y))
    
def reduce_fraction(numerator, denominator):
    gcf = GCF(numerator, denominator)
    numerator = numerator / gcf
    denominator = denominator / gcf
    return numerator, denominator
    
def to_roman(x):
    if 0 >= x < 4000:
        raise ValueError
    roman = (( 'M' , 1000),
             ('CM',   900),
             ( 'D' ,  500),
             ('CD',   400),
             ( 'C' ,  100),
             ('XC',    90),
             ( 'L' ,   50),
             ('XL',    40),
             ( 'X' ,   10),
             ('IX',     9),
             ( 'V' ,    5),
             ('IV',     4),
             ( 'I' ,    1))
    output = ''
    for key, value in roman:
        while x >= value:
            output += key
            x -= value
    return output
