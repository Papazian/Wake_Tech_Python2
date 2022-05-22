
# Description: Given a phrase, output an encrypted string of the phrase that is Caesar Shifted by an integer
# Date: 4/9/2016



# Define function to encrypt the original text using a Caesar Cipher of N
def encrypt(original_text,shift_by_N):
	encrypted_text=""								# Default encrypted text is empty
	for i in original_text:							# Loops through each character in original text
		encrypted_text += chr(ord(i) + shift_by_N)	# The encrypted character is the character value of the (ASCII number + N)
	return(encrypted_text)							# Return the encrypted text


while True:

	# Try to retrieve an integer input from user
	try:
		N = int(raw_input("\nPlease enter a number from 1 to 100: "))
		if ((N >= 1) and (N <= 100)):
			phrase = raw_input("Please enter a phrase to encrypt: ")
			print encrypt(phrase,N)
		else:
			print "\nPlease try again!"
	
	except Exception as msg:
		print "\nPlease try again!"

