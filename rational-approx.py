# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 18:11:26 2026

@author: frank chemotti
fchemotti@gmail.com

Find rational approximations of decimal numbers with limited prime factors.
"""

import itertools

primes = [2, 3, 5, 7] 
exponent_limit = 4
target = 3.3103
error = 0.005 # relative error, percentage-wise
lower = target / (1 + error)
upper = target * (1 + error)
output_precision = 4

exponents = list(range(-exponent_limit, exponent_limit + 1))
exponent_combos = itertools.product(exponents, repeat=len(primes))

def get_fraction(primes, exp):
    num_str = ''
    num = 1
    den_str = ''
    den = 1
    for (p, e) in zip(primes, exp):
        if e == 0: # p does not appear in the fraction
            pass
        elif e > 0: # p appears in numerator
            if num_str:
                num_str = num_str + ' '
            num_str = num_str + str(p) + '^' + str(e)
            num = num * (p ** e)
        elif e < 0: # p appears in denominator
            if den_str:
                den_str = den_str + ' '
            den_str = den_str + str(p) + '^' + str(-e)
            den = den * (p ** -e)
    if not num_str:
        num_str = '1'
    if not den_str:
        den_str = '1'
    factors_str = num_str + ' / ' + den_str
    return (num, den, factors_str)

answers = []

for exp in exponent_combos:
    (num, den, factors_str) = get_fraction(primes, exp)
    decimal = num / den
    if lower <= decimal and decimal <= upper and (num, den) not in answers:
        answers.append((num, den))
        fraction_str = str(num) + ' / ' + str(den)
        dr = round(decimal, output_precision)
        er = round((decimal / target) - 1, output_precision)
        #print (fraction_str, '=', factors_str, '=', dr, '  err:', er)
        print(f"{fraction_str:<20}{'= ' + factors_str:<25}{'= ' + str(dr):<15}{'err: ' + str(er):<15}")
                
        
        

