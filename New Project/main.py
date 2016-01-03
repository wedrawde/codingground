    # Open a file
    fo = open("foo.txt", "w+")

    for n in xrange(1,N,2): # odd number
        for m in xrange(1,n,2): # odd number less than n
            (a,b,c)=(n*m, (n+m)*(n-m)/2, (n+m)*(n+m)/2-n*m)
            if (n-m-2*m*m < 0):
                (a,b)=(b,a) # swap a,b
            if (fractions.gcd(m,n) == 1): # prime
                fo.write("%d;%d;%d\n" % (a,b,c))

    # Close opend file
    fo.close()
