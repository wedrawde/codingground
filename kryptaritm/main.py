# Hello World program in Python
# abcd*abcd= xxxxabcd

import math

def doit():
    for x in xrange(1,999999999): # alla tal
        if ((x**2)%(10**int(math.log10(x)+1)) == x): # x*x = x (mod 10**n)
            print x,(x**2)

def test1(a):
    t=10**int(math.log10(a)+1)
    print "x%d"%a,"->",
    for x in [1,2,3,4,5,6,7,8,9]:
        print "%d%d"%(x,((x*t+a)**2)%(t)),
    print
    print "x%d"%a,"->",
    for x in [1,2,3,4,5,6,7,8,9]:
        print "%d"%(((x*t+a)**2)%(10*t)),
    print
    print    

def t2(a):
    print a**2
    print a*(a-1)

def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        return quick_sort([e for e in l[1:] if e <= l[0]]) + [l[0]] +\
            quick_sort([e for e in l[1:] if e > l[0]])

# Main
# doit()

print quick_sort([2,4,6,4,5,7,4,3,5,7])


t2(3740081787109376)

# for x in [5,6,25,76,376,625,87109376,212890625]):
#    test1(x)
# print

619541169787109376
