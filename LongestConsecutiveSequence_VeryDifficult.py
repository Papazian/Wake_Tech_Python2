
# Description: Given an unsorted array of integers, find the length of the longest consecutive elements sequence
# Date: 4/23/2016



while True:

	try:
	
		# Retrieve input as space separated integers
		input_list = raw_input("\nPlease enter space separated numbers: ").split()
		number_list = [int(a) for a in input_list] 
		
		# Sort the list of integers
		number_list.sort()

		# Initialize variables
		last_number = number_list[0]
		sequence_count = 1
		max_sequence_count = 1
		
		# Loop through each number of the list of numbers
		for number in number_list:
			# If the current number is consecutive from last number, then increment the sequence count
			if (number==(last_number+1)):
				sequence_count += 1
				# If the current sequence count is the highest, then record that in the max sequence count
				if (sequence_count>max_sequence_count):
					max_sequence_count=sequence_count
			# Else if the current number is the same the last number, then don't reset the sequence count
			elif (number==last_number):
				sequence_count = sequence_count
			# Otherwise, reset the sequence count
			else:
				sequence_count = 1
			# Record the current number as the "last number" to use in the next iteration of the loop
			last_number = number
		
		# Print the length of the longest consecutive elements sequence
		print max_sequence_count
				
	except Exception as msg:
		print "\nPlease try again!"