# Primitive pythagorean triples program in Python
# (c) 2016 Edward Krogius
# 
# Take odd integers 0 < m < n 
# if m < N then if gcd(m,n) != 1 print (n+m)(n-m)/2, nm, (n+m)(n+m)/2 - nm
#
import math

def main():
    N=10
    for n in xrange(1,N,2):
        for m in xrange(1,n,2):
            print n,m

if __name__ == '__main__':
    main()
