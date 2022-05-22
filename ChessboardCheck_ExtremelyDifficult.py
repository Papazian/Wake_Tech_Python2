
# Description: Returns true if your king is in check, otherwise it returns false
# Date: 4/30/2016



# Define one and only one function that takes a list as a parameter and returns True if your king is in check, otherwise it returns False
def kingIsInCheck(board):
	try:
		
		# Loop through every cell in matrix of chessboard to look for king and queen
		for i in range(len(board)):
			for j in range(len(board[0])):
				if (board[i][j]=="K" or board[i][j]=="k"):
					kingRow = i
					kingCol = j
				elif (board[i][j]=="Q" or board[i][j]=="q"):
					queenRow = i
					queenCol = j
		
		# Return true if king and queen are the located the same horizontally, vertically, or diagonally
		if ((kingRow==queenRow) or (kingCol==queenCol) or (abs(kingRow-queenRow)==abs(kingCol-queenCol))):
			return True
		else:
			return False
			
	except Exception as msg:
		print "\nChessboard is not valid!"



# Creatre a sample chessboard to test out function
board = [["","","",""],["","K","",""],["","","",""],["","","","Q"]]

# Display the sample chessboard in order to visualize the test case
for i in range(len(board)):
	print "-----------------"
	chessrow = "|"
	for j in range(len(board[0])):
		if (board[i][j]=="K" or board[i][j]=="k"):
			chessrow += " K |"
		elif (board[i][j]=="Q" or board[i][j]=="q"):
			chessrow += " Q |"
		else:
			chessrow += "   |"
	print chessrow
print "-----------------"

# Print out the test results
print "Test Case: Is the king in check? ", kingIsInCheck(board)

	


