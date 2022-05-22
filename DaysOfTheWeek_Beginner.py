
# Description: Given a string that represents a day of the week, return whether or not you will be sleeping in
# Date: 4/2/2016



while True:

	text_input = raw_input("\nPlease enter a day: ")
	text_output = ""

	if (text_input == "Monday"):	
		text_output = "You will work"
	elif (text_input == "Tuesday"):	
		text_output = "You will work"
	elif (text_input == "Wednesday"):	
		text_output = "You will work"
	elif (text_input == "Thursday"):	
		text_output = "You will work"
	elif (text_input == "Friday"):	
		text_output = "You will work"
	elif (text_input == "Saturday"):	
		text_output = "You will sleep in"
	elif (text_input == "Sunday"):	
		text_output = "You will sleep in"
	else:
		text_output = "That is not a valid day"

	print text_output
