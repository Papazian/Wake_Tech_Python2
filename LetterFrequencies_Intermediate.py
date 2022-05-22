
# Description: Given a phrase, return exactly how many times all 26 letters appear in that phrase.
# Date: 4/9/2016



while True:

	# initialize dictionary to store count of letters
	dictLetters = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}

	# retrieve phrase from user 
	phrase = raw_input("\nPlease enter a string: ")
	
	# loop through each letter in phrase and update the count in dictionary
	for letter in phrase:
		if ((ord(letter)>=97) and (ord(letter)<=122)):	# if lower case letter
			dictLetters[letter] += 1		
		elif ((ord(letter)>=65) and (ord(letter)<=90)):	# else if upper case letter
			dictLetters[chr(ord(letter)+32)] += 1		
		else:											# else not a letter
			pass										

	# loop from chr(97) i.e. 'a' to chr(122) i.e. 'z' and print the count of letters
	for i in range(97,122+1):			
		print chr(i), ": ", dictLetters[chr(i)]