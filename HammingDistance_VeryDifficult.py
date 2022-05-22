
# Description: Return the number of bits that differ between the binary representation of two integers
# Date: 4/23/2016



while True:

	try:
	
		# Try to retrieve two values from user and convert them into integers
		a_string,b_string = raw_input("\nPlease enter two space separated integers: ").split()
		a = int(a_string)
		b = int(b_string)

		# Convert the base 10 integers into base 2 binary integers (using eight bytes), and then into strings
		# http://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python
		a_binary = bin(a)[2:].zfill(64)
		b_binary = bin(b)[2:].zfill(64)
		a_binary_string = str(a_binary)
		b_binary_string = str(b_binary)

		# Initialize variables
		hamming_distance = 0
		bit_count = 0
		
		# Loop through each bit in the eight bytes
		while (bit_count < 64):
			# If the bits are the same, then don't change the hamming distance 
			if (a_binary_string[bit_count] == b_binary_string[bit_count]):	
				hamming_distance += 0
			# Else the bits are different, so increment the hamming distance
			else:											
				hamming_distance += 1
			# Increment the bit count to reference the next bit in the eight bytes
			bit_count += 1
				
		print hamming_distance
				
	except Exception as msg:
		print "\nPlease try again!"