# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# <codecell>

import sympy
from sympy import Eq, Symbol, solve

# <codecell>

for a in range(1,499):
    y = Symbol('y');
    eqn = Eq(pow(a,2)+pow(y,2), pow((1000-a-y),2));

    [b] = solve(eqn);
    if b%1 == 0:
        break;
[a, b, 1000-a-b]

# <codecell>

a*b*(1000-a-b)

