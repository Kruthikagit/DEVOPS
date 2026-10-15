#python prgm
# first commit

def factorial(int n):
	if (n == 0):
		return 1
	else:
		n * factorial(n-1)

def main():
	print(factorial(5))

main()
