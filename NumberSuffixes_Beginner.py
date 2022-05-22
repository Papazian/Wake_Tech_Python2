
# Description: Given a number from the user and add the corresponding chronological suffix
# Date: 4/2/2016



while True:

	text_input = raw_input("\nPlease enter a number: ")
	number_suffix = ""
	
	try:
		value = int(text_input)		# proceed only if the input is an integer
		
		last_digit = text_input[-1:]
		last_two_digits = text_input[-2:]
		
		if (last_digit == "1"):	
			if (last_two_digits == "11"):
				number_suffix = "th"
			else:
				number_suffix = "st"
		elif (last_digit == "2"):	
			if (last_two_digits == "12"):
				number_suffix = "th"
			else:
				number_suffix = "nd"
		elif (last_digit == "3"):	
			if (last_two_digits == "13"):
				number_suffix = "th"
			else:
				number_suffix = "rd"
		else:
			number_suffix = "th"
			
		print text_input + number_suffix
		
	except ValueError:
		pass  	# it was not an integer, so pass