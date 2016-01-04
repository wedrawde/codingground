# Hello World program in Python

import time

def m28433():
    return (28433 * 2**7830457 + 1) % 10000000000

print "Mersenne prime M28433 10 last digits"

start = time.time()
prime = m28433()
elapsed = (time.time() - start)

print "found %s in %s seconds" % (prime,elapsed)
