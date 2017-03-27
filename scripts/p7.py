# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

# <codecell>

def isprime(n):
    ans = 0;
    if n == 2 or n == 3:
        ans = 1;
    elif n <= 1 or n == 4 or n%2==0:
        ans = 0;
    else:
        cand = range(3,n,2);
        ans = 1;
        for ii in cand:
            if n%ii == 0:
                ans = 0;        
    return ans
isprime(101)

# <codecell>

def euler7(n):
    k = [0];
    ii = 1;
    while sum(k) < n:
        k = k + [isprime(ii)];
        ii = ii + 1;   
    return ii-1
euler7(100)

# <codecell>

import sets
from sets import Set

# <codecell>

x = range(10);
y = range(1,10,2);
Set(x).difference(Set(y))

# <codecell>

def diff(a, b):
        b = set(b)
        return [aa for aa in a if aa not in b]

# <codecell>

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

ans = erasto(10000);
ans = erastoIter(ans,10000,120000);
ans[10001]

# <codecell>

len(ans)

# <codecell>

newAns = erastoIter(ans,

# <codecell>

newAns[10001]

# <codecell>

newCand = range(50001,100000);
for ii in ans:
    mult = filter(lambda x: x >50000, range(ii, 100000, ii) );
    newCand = diff(newCand, mult);

ans = ans+newCand;
len(ans)
    

# <codecell>

newCand = range(100001,120000);
for ii in ans:
    mult = filter(lambda x: x >100000, range(ii, 120000, ii) );
    newCand = diff(newCand, mult);

ans = ans+newCand;
len(ans)
    

# <codecell>

ans[0]

# <codecell>

ans[10001]

# <codecell>

ans = erasto(10000);
len(ans)

# <codecell>

newAns =erastoIter(ans,20000,50000);
len(newAns)

# <codecell>

ans[0]

# <codecell>

newAns[0:10]

# <codecell>


