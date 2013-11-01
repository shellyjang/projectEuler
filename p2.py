t = [1]
while t[-1] < 4000000:
    t.append(sum(t[-2:]))   
r = [t[ii] for ii in range(len(t)) if t[ii]%2==0]
print sum(r)
