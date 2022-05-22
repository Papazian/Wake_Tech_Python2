
# Description: Given a string, print 1 if brackets are correctly matched else print 0
# Date: 4/9/2016



while True:

	text_input = raw_input("\nPlease enter a string: ")
	
	correctly_matched = 1	# assume brackets are correctly matched until shown otherwise
	bracket_stack = 0		# number of brackets on the "stack"

	for i in text_input:		# Loop through each character in text string
		if (i == '('):	
			bracket_stack += 1		# push a bracket onto the stack
		elif (i ==')'):
			bracket_stack -= 1		# pop a bracket off the stack
			if (bracket_stack < 0):		# if we ever pop off bracket before pushing a bracket onto stack,
				correctly_matched = 0	# then there must be a mismatch, so set the condition to false
		else:
			bracket_stack = bracket_stack		# do nothing

	if (correctly_matched==0):		# if we know there is a mismatch, then go ahead and alert the user
		print correctly_matched	
	else:							# otherwise, check to see if all brackets have been popped off the stack
		if (bracket_stack==0):
			print correctly_matched		# if stack is empty, then print that all brackets are correctly matched
		else:
			correctly_matched=0			# if stack is not empty, then alert user of the mismatch
			print correctly_matched
		
