
# Description: ask the user for a mass and an acceleration and then print out the force
# Date: 4/9/2016



# Define function that takes two parameters, mass and acceleration, and then returns the force
def CalculateForce(mass,acceleration):
	return(mass * acceleration)

	
while True:

	# Try to retrieve two floating point inputs, and then print the output of function
	try:
		m = float(raw_input("\nPlease enter the mass (in kilograms): "))
		a = float(raw_input("Please enter the acceleration (in meters per second^2): "))
		print "The force is ", CalculateForce(m,a), " Newtons"
	
	except Exception as msg:
		print "\nPlease try again!"
