#!/usr/bin/python
# coding: iso-8859-1

# Primitive pythagorean triples program in Python
# (c) 2016 Edward Krogius
# 
# Take odd integers 0 < m < n 
# if m < N then if gcd(m,n) != 1 print (n+m)(n-m)/2, nm, (n+m)(n+m)/2 - nm
#
# Product: 31875000 (with 200+375+425=1000 and n=25)                                                                                                                                                 
# Time: 0.00009 seconds   
#

import math, fractions, time

def triples():
    start=time.time()

    pts=[] # list of all primitive triples
    N=100   # s=a+b+c=1000 <= 2n^2 => N < 26 
    (nn,mm)=(0,0) # For storing results 
    
    for n in xrange(1,N,2): # odd number
        for m in xrange(1,n,2): # odd number less than n
            if (n*(n+m) == 1000): # the sum a+b+c = n*n+n*m = S = 1000
                (nn,mm) = (n,m)
            # Save the primitive triples ( for use later)        
            if (fractions.gcd(m,n) == 1): # n and m are coprime
                (a,b,c)=(n*m, (n*n-m*m)/2, (n*n+m*m)/2)
                if (float(a*b)/c==a*b//c):
                    print float(a*b)/c
                if (n-m-2*m*m < 0):
                    (a,b)=(b,a) # swap a,b for a>b
                pts.append([c,b,a]) # hypotenuse first

    pts.sort()
    for triple in pts: # returns list of primitive triples
        print triple 
        
    (a,b,c)=(nn*mm, (nn+mm)*(nn-mm)/2, (nn+mm)*(nn+mm)/2-nn*mm)
    if (nn-mm-2*mm*mm < 0): 
        (a,b)=(b,a) # swap a,b
    
    print "Product: {}".format(a*b*c),
    print "(with %d+%d+%d=1000 and n=%d)" % (a,b,c,nn)
    elapsed = time.time() - start
    print "Time: {:.5f} seconds".format(elapsed)

if __name__ == '__main__':
    triples()
