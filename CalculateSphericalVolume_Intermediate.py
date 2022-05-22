
# Description: Calculate the volume of a sphere using the formula in a function
# Date: 4/9/2016



# Define function to calculate the volumne of a sphere
def SphericalVolume(radius):
	pi = 3.14159
	return( (4.0/3.0) * pi * (radius**3) )

	
while True:

	# Try to retrieve a float input, and then print the output of function
	try:
		r = float(raw_input("\nPlease enter the radius of the sphere: "))
		print "The volume of the sphere is ", SphericalVolume(r)
	
	except Exception as msg:
		print "\nPlease try again!"

