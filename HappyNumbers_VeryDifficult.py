
# Description: Determine if a number is a happy number
# Date: 4/23/2016



while True:

	try:
		# Try retrieve an integer from user 
		number = int(raw_input("\nPlease enter a number: "))
		original_number = number

		# Initialize variables
		happy = False
		seen_before = False
		sum_of_squares_of_digits = 0
		my_set = set()

		# Continue to loop while (1) the number is not happy and (2) we have not seen the number before
		while (happy==False and seen_before==False):

			# loop through each character in number
			for character in str(number):
				# if character is a digit, then sum the digits squared
				if ((ord(character)>=48) and (ord(character)<=57)):	
					sum_of_squares_of_digits += int(character)**2
				# else character is not a digit so ignore
				else:											
					pass											

			# If the "sum of the digits squared" equals 1 then original number is happy		
			if (sum_of_squares_of_digits==1):	
				happy=True
			# Else continue the while loop with the "sum of the digits squared" as new number
			else:								
				happy=False
			
			# If the "sum of the digits squared" exists in set, then we have seen it before
			if (sum_of_squares_of_digits in my_set):	
				seen_before=True
			# Else add the "sum of the digits squared" to the set
			else:								
				seen_before=False
				my_set.add(sum_of_squares_of_digits)
			
			# Prepare for the next iteration of loop
			number = str(sum_of_squares_of_digits)
			sum_of_squares_of_digits = 0
		
		# After the loop ends, print if the number is happy or not
		if (happy==True):
			print 1
		else:								
			print 0

	except Exception as msg:
		print "\nPlease try again!"