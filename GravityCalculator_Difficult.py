
# Description: Output the force of gravity between the two objects
# Date: 4/16/2016



# Define function that takes three parameters (distance, mass1, & mass2) and then returns the force of gravity
def CalculateGravity(distance,mass1,mass2):
	return( (6.674*(10**-11)) * ( (mass1*mass2) / (distance**2) ) )


while True:

	# Try to retrieve three floating point inputs, and then print the output of function
	try:
		d = float(raw_input("\nPlease enter the distance of the bodies (in meters): "))
		m1 = float(raw_input("Please enter the mass of the first body (in kilograms): "))
		m2 = float(raw_input("Please enter the mass of the second body (in kilograms): "))		
		print "The gravity is ", CalculateGravity(d, m1, m2), " Newtons"
	
	except Exception as msg:
		print "\nPlease try again!"
