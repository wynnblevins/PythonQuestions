import sys

def fizzbuzz(number):
	if number % 3 == 0 and number % 5 == 0:
		print("FizzBuzz")
	elif number % 3 == 0:
		print("Fizz")
	elif number % 5 == 0:
		print("Buzz")
	else: 
		print(number)
		
def runFizzBuzz(number):
	for i in range(1, number):
		fizzbuzz(i)
		
upperLimit = sys.argv[1]		
runFizzBuzz(int(upperLimit))