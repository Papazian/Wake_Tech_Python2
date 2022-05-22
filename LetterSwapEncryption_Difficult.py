
# Description: Encrypts messages by swapping all L's for D's and all D's for L's
# Date: 4/16/2016



# Define function to encrypt messages by swapping all L's for D's and all D's for L's
def encrypt(original_text):
	encrypted_text=""						# Default encrypted text is empty
	for i in original_text:					# Loops through each character in original text
		if (i=="l" or i=="L"):
			encrypted_text += "d"			# Swaps all L's for D's
		elif (i=="d" or i=="D"):
			encrypted_text += "l"			# Swaps all D's for L's
		else:
			encrypted_text += i
	return(encrypted_text.lower())			# Return the encrypted text in lower case


# Try to retrieve message input from user
while True:
	try:
		phrase = raw_input("\nPlease enter a message: ")
		print encrypt(phrase)
	except Exception as msg:
		print "\nPlease try again!"
