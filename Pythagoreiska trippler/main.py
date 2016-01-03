# Primitive pythagorean triples program in Python
# (c) 2016 Edward Krogius
# 
# Take odd integers 0 < m < n 
# if m < N then if gcd(m,n) != 1 print (n+m)(n-m)/2, nm, (n+m)(n+m)/2 - nm
#
import math, fractions

def main():
    N=10
    for n in xrange(1,N,2): # odd number
        for m in xrange(1,n,2): # odd number less than n
            (a,b,c)=(n*m, (n+m)*(n-m)/2, (n+m)*(n+m)/2-n*m)
            if (n-m-2*m*m < 0):
                (a,b)=(b,a) # swap a,b
            if (fractions.gcd(m,n) == 1): # prime
                print " (%d:%d:%d), " % (a,b,c),"\t",
            else:
                print "\n"
        print

if __name__ == '__main__':
