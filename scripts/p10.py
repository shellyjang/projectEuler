# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import sets
from sets import Set

def diff(a, b):
        b = set(b)
        return [aa for aa in a if aa not in b]
    
def erasto(n):
    cand = range(2,n+1);
    ii = 0;
    p = cand[ii];
    cand = diff(cand, range(2*p, n+1, p));
    while p < max(cand): 
        ii = 0;
    #    p = cand[ii];
    #   cand = diff(cand, range(2*p, n+1, p));
        while ( p >= cand[ii] ):
            ii = ii+1;
        p = cand[ii];
        cand = diff(cand, range(2*p, n+1, p));
    return cand

def erastoIter(prev,min,max):
    newCand = range(min, max);
    for ii in prev:
        mult = filter(lambda x: x > min, range(ii, max, ii));
        newCand = diff(newCand, mult);
    ans = prev + newCand;
    return ans

# <codecell>

ans = erasto(10000);
ans = erastoIter(ans,10000,120000);
ans = erastoIter(ans,120000,300000);

# <codecell>

ans = erastoIter(ans,300000,1000000);

# <codecell>

ans[-1]

# <codecell>

newAns = erastoIter(ans,300000,600000);

# <codecell>

ans[-1]

# <codecell>

import numpy
def sieveOfErat(end):  
  if end < 2: return []  

  #The array doesn't need to include even numbers  
  lng = ((end/2)-1+end%2)  

  # Create array and assume all numbers in array are prime  
  sieve = [True]*(lng+1)  

  # In the following code, you're going to see some funky  
  # bit shifting and stuff, this is just transforming i and j  
  # so that they represent the proper elements in the array.  
  # The transforming is not optimal, and the number of  
  # operations involved can be reduced.  

  # Only go up to square root of the end  
  for i in range(int(pow(end,0.5)) >> 1):  

    # Skip numbers that aren’t marked as prime  
    if not sieve[i]: continue  

    # Unmark all multiples of i, starting at i**2  
    for j in range( (i*(i + 3) << 1) + 3, lng, (i << 1) + 3):  
      sieve[j] = False  

  # Don't forget 2!  
  primes = [2]  

  # Gather all the primes into a list, leaving out the composite numbers  
  primes.extend([(i << 1) + 3 for i in range(lng) if sieve[i]])  

  # return primes
  return range(int(pow(end,0.5))) >> 1

# <codecell>

10 >> 5

# <codecell>

sum(primes)

# <codecell>

print f >> "Hello World"

# <codecell>

for i in range(int(pow(100,0.5)) >> 1): 
    print i

# <codecell>

range(int(pow(100,0.5)) >> 1)

# <codecell>

int(pow(100,0.5)) >> 1

# <codecell>

def div2(n):
    return n/2;
def rightShift(n):
    return round(n/2);

# <codecell>

map(rightShift, range(int(pow(100,0.5))))

# <codecell>

map((lambda x: round(x/2)), range(int(pow(100,0.5))))

# <codecell>


