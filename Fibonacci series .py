import random
n = 15

def fibonacci(n):
    
	#fibonacci sequence. 
	
	if (n <= 1):
		return n

	else:
		fib_sum = fibonacci(n - 1) + fibonacci(n-2)
		return fib_sum


def fizzbuzz(n):
	#checking divisibility
	
	fibonacci_s = ""

	if (isPrime(n)):
		return "BuzzFizz"

	if (n%3 == 0):
		fibonacci_s += "Fizz"

	if (n%5 == 0):
		fibonacci_s += "Buzz"

	if fibonacci_s == "":
		return n
	
	return fibonacci_s

def isPrime(n):
	
	# checking for prime.
	
	limit = int(n**0.5) + 1

	if n < 2:
		return False
	if ( (n > 2) and (n%2 == 0) ): 
		return False
	for i in range(3, limit, 2):
		if n % i == 0:
			return False

	return True

if __name__ == "__main__":
	fib_print = []
	fb_print = []
	
	for f in range(0, n):
		fib_sum = fibonacci(f)
		fb = fizzbuzz(fib_sum)

		fib_print.append(fib_sum)
		fb_print.append(fb)
		
	print "Fibonacci - #" + str(n), "=", fib_print
	print "Fizzbuzz:"
	for r in range(0, n):
		print fib_print[r], "->", fb_print[r]