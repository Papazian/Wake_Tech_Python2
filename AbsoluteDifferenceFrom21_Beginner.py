

# Description: Given an integer n as input, return the absolute difference between n and 21, 
#              except return double the absolute difference if n is over 21
# Date: 4/2/2016



while True:

	n = int(raw_input("\nPlease enter a number: "))

	if (n <= 21):		
		print abs(21-n)
	else:
		print 2*(abs(n-21))
