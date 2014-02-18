# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

def triangle(num):
     return sum(xrange(num+1))
triangle(7)

# <codecell>

ii = 2;
p = num%ii
if p == 0:
    divs.append(ii)

# <codecell>

def divisors(num):
    divs = list();
    for ii in xrange(2, long(round((num+1)/2))):
        p = num%ii;
        if ii in divs:
            break
        if p == 0:
            divs.append(ii);
            divs.append(num/ii);
        
    return divs
divisors(36)
        

# <codecell>

len(unique(divisors(1000)))

# <codecell>

def euler12(num):
    return len(unique(divisors(num)))

euler12(100)

# <codecell>

num = long(100);
k = euler12(num)

while k < 500:
    num = num * 2
    k = euler12(num)
    print k, num

# <codecell>

euler12(long(pow(10,11)))

# <codecell>

import operator

def wowrange(start, stop, step=1):
  if step == 0:
    raise ValueError('step must be != 0')
  elif step < 0:
    proceed = operator.gt
  else:
    proceed = operator.lt
  while proceed(start, stop):
    yield start
    start += step

# <codecell>

wowrange(1,long(pow(10,11)))

def euler12_re(num):
    divs = list();
    for ii in wowrange(2, long(round((num+1)/2))):
        p = num%ii;
        if ii in divs:
            break
        if p == 0:
            divs.append(ii);
            divs.append(num/ii);
        
    return len(unique(divs))

# <codecell>

k = 223 #euler12_re(pow(10,14))

# <codecell>

num = 14
while k < 500:
    num += 1
    k = euler12_re(pow(10,num))
    print k, num

