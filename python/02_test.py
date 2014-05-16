principle = 1000
rate = 0.05
numyear = 12
year = 1

while numyear > year:
	principle = principle * (1 + rate)
	print("%5d %0.2f" % (year, principle))
	year += 1

bool_value = True
bool_value = False

if (bool_value):
	print("it is true")
else: 
	print('it is false ... ')

num = 5

if (num > 5):
	print('num is greater than 5')
elif (num > 3):
	print('still greater than 3')
else: 
	print('oh .. less than 3')

print("=======================================================================")
f = open('test.txt')
line = f.readline()
while line: 
	print(line, end="")
	line = f.readline()

f.close()
print("")
print("=======================================================================")

try:
	anum = int(input("tell me your age?"))
except:
	print('please enter a valid integer')
	anum = 0

if anum > 0:
	if anum > 40:
		print('man, you are old')
	elif anum > 20:
		print('right on')
	else:
		print('meh, still rookie')


astring = ''' this is cool and it's ok
I like it
so am I '''

print(astring)
