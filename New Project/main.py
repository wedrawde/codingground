# Hello World program in Python

import math                                                                

N=5000

def pythagorean_triples(n):                                                
    a, b, c, d = 1, 3, 0, 0
    while (c < n) and (d<=1000):                                                            
        a_ = (a * b) + a                                                    
        c = math.sqrt(a_**2 + b**2)   
        d=a_+b+ int(c)
        
        if c == int(c):                                                    
            yield b, a_, int(c), d                               
        a += 1                                                              
        b += 2                                                              
 
if __name__ == '__main__':                                                  
    import sys                                                              
    for pt in pythagorean_triples(N):                        
        print(pt)
