# Hello World program in Python

import math

def main():
    N=100
    for x in xrange(1,N):
        y = x+1
        z = y+1
        while (z <= N):
            while (z * z < x * x + y * y ):
                z = z + 1
                if (z * z == x * x + y * y) and (z <= N):
                    print z # use x, y, z, (y-z)*(y-z) 
                    y = y + 1

if __name__ == '__main__':
    main()
