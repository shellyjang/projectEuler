def euler6(n):
    ans = 0;
    for ii in range(1,n):
        ans = ans + 2*ii*sum(range(ii+1,n+1));
    return ans
