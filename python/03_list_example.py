import sys # Load the sys module

# to execute: python 03_list_example.py test.dat

if len(sys.argv) != 2: # Check number of command line arguments :
	print("Please supply a filename")
	raise SystemExit

f = open(sys.argv[1]) # Filename on the command line
svalues = f.readlines() # Read all lines into a list
f.close()
# Convert all of the input values from strings to floats
fvalues = [float(s) for s in svalues]
# Print min and max values
print ("The minimum value is ", min(fvalues))
print ("The maximum value is ", max(fvalues))
