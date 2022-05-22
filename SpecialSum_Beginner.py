
# Description: Given two integer values separated by a space, return their sum.
#              Unless the two values are the same, then return double their sum. 
# Date: 4/2/2016



while True:

	var1, var2 = raw_input("\nPlease enter two integers: ").split()

	try:		# try to cast the two variables as integers before we procede 
		var1, var2 = [int(var1), int(var2)]
		if (var1==var2):		
			print 2*(var1+var2)
		else:
			print var1+var2
			
	except ValueError:
		pass  	# the variables are not integers
