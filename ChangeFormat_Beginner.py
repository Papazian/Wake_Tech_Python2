
# Description: Given a string, replace each space within the string with '%20'
# Date: 4/2/2016



while True:

	text_input = raw_input("\nPlease enter a string: ")
	text_output = ""

	for i in text_input:		# Loops through each character in text string
		if (i == ' '):	
			text_output += '%20'
		else:
			text_output += i

	print text_output
