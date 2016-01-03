# Primitive pythagorean triples program in Python
# (c) 2016 Edward Krogius
# 
# Take odd integers 0 < m < n 
# if m < N then if gcd(m,n) != 1 print (n+m)(n-m)/2, nm, (n+m)(n+m)/2 - nm
#
import math, fractions

def main2():
    N=1000000
    s=0
    for n in xrange(1,N,2): # odd number
        for m in xrange(1,n,2): # odd number less than n
            if (fractions.gcd(m,n) == 1): # prime
                s+=1
    print s
         
if __name__ == '__main__':
    main2()