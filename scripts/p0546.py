import numpy as np 

def fun(k, n):
	a = [ii/k  for ii in np.arange(1, n+1)]
	return np.sum(a) + 1
	

if __name__ == '__main__':
	print fun(5, 10)
