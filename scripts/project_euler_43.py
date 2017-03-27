import numpy as np
import pandas as pd 

def three_digit_long_multiples(d, columns):
	multiple = np.array([[ii for ii in '{:03d}'.format(d*n)] for n in np.arange(9/d, 999/d) if len(list(set('{:03d}'.format(d*n)))) == 3])
	multiple = pd.DataFrame(multiple, columns=columns)
	return multiple

def main():
	"""
	The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

	Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

	d2d3d4=406 is divisible by 2
	d3d4d5=063 is divisible by 3
	d4d5d6=635 is divisible by 5
	d5d6d7=357 is divisible by 7
	d6d7d8=572 is divisible by 11
	d7d8d9=728 is divisible by 13
	d8d9d10=289 is divisible by 17
	Find the sum of all 0 to 9 pandigital numbers with this property.
	"""

	divisors = [17, 13, 11, 7, 5, 3, 2]
	multiple17 = three_digit_long_multiples(17, ['d8','d9','d10'])

	multiple13 = three_digit_long_multiples(13, ['d7','d8','d9'])

	multiple11 = three_digit_long_multiples(11, ['d6','d7','d8'])

	multiple7 = three_digit_long_multiples(7, ['d5','d6','d7'])

	multiple5 = three_digit_long_multiples(5, ['d4','d5','d6'])

	multiple3 = three_digit_long_multiples(3, ['d3','d4','d5'])

	multiple2 = three_digit_long_multiples(2, ['d2','d3','d4'])

	pandigital = multiple17.merge(multiple13)
	pandigital = pandigital.merge(multiple11)
	pandigital = pandigital.merge(multiple7)
	pandigital = pandigital.merge(multiple5)
	pandigital = pandigital.merge(multiple3)
	pandigital = pandigital.merge(multiple2)

	pandigital = pandigital[pandigital.apply(lambda x: x.nunique()==9, axis=1)]

	pandigital['d1'] = pandigital.apply(lambda x: [d for d in np.arange(10) if str(d) not in x.tolist()][0], axis=1)
	pandigital['d1'] = pandigital['d1'].astype(str)

	pandigital = pandigital[['d{}'.format(m) for m in range(1, 11)]]
	pandigital['int'] = pandigital.apply(lambda x: ''.join(x.tolist()), axis=1).astype(int)

	return pandigital['int'].sum()

def alt1():
	digits = ['1','2','3','4','5','6','7','8','9','0']
	divisors = [13, 11, 7, 5, 3, 2, 1]
	res = []
	res1 = []

	j = 1
	while j*17 < 1000:
	    N = j*17
	    Nstr = str(N)
	    if len(set(Nstr)) == len(Nstr):
	        if N < 100: res.append('0' + str(N))
	        else: res.append(str(N))
	    j += 1

	for div in divisors:
	    for Nstr in res:
	        for d in digits:
	            if d not in Nstr:
	                Newstr = d + Nstr[:2]
	                if int(Newstr)%div == 0:
	                    res1.append(d + Nstr)

	    res = res1
	    res1 = []

	tot = 0
	for Nstr in res:
	    print Nstr
	    tot += int(Nstr)

	print
	print tot

if __name__ == '__main__':
	print main()
	# alt1()
