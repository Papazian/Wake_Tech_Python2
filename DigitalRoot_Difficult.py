
# Description: Given a positive number, return the single digit obtained by repeatedly adding all its digits until the result has only one digit
# Date: 4/16/2016



while True:

	try:
		# Try retrieve an integer from user 
		number = int(raw_input("\nPlease enter a number: "))
		original_number = number

		# Initialize variables
		single_digit_yet = False
		sum_of_digits = 0

		while (single_digit_yet==False):

			# loop through each character in number
			for character in str(number):
				if ((ord(character)>=48) and (ord(character)<=57)):	
					sum_of_digits += int(character)				# if character is a digit then sum the digits
				else:											
					pass										# else character is not a digit so ignore

			if (len(str(sum_of_digits))==1):	# if the sum is a single digit then exit while loop
				single_digit_yet=True
			else:								# else continue the while loop with the sum of digits as the new number
				single_digit_yet=False
				number = str(sum_of_digits)
				sum_of_digits = 0
			
		print "\nThe digital root of ", original_number, " is ", sum_of_digits
		
	except Exception as msg:
		print "\nPlease try again!"