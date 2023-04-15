#first value is speed - m/s
#second value is distance - m
# seconds = m / m/s = m * s/m = s
# time = distance / speed

# Recommended imports for all problems
# Some problems may require more
import sys
import math
import string

# Always start with reading in the number
# of test cases from standard input. The
# rstrip() method removes the lingering newline
cases = int(sys.stdin.readline().rstrip())

# Loop for each test case. This is the last line
# common to all problems; the content of this
# loop will change based on the problem solved.
for caseNum in range(cases):  #= for caseNum in range(2) - 0, 1; range(5) = 0, 1, 2, 3, 4
	# For problem A, we're just spitting out
	# the input as it's written
	input = sys.stdin.readline().rstrip()
	parsed = input.split(":") 
	speed = float(parsed[0])
	distance = float(parsed[1])

	if(speed == 0):
		print("SAFE")
	else: 
		time = distance / speed
		if(time <= 1): #true/false
			print("SWERVE")
		elif(time <= 5):	
			print("BRAKE")				#else if()
		else:
			print("SAFE")
