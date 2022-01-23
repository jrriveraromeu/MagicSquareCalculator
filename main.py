import pyfiglet
from termcolor import colored

ascii_banner = pyfiglet.figlet_format("msqrl")
ascii_banner_clear = ascii_banner.rstrip()
print(ascii_banner_clear)
print(colored('Magic Squares Generator', 'red'))

def generateSquare(n):
	magicSquare = [[0 for x in range(n)] for y in range(n)]

	i = n / 2
	j = n - 1
	num = 1

	while num <= (n * n):
		if i == -1 and j == n: 
			j = n - 2
			i = 0

		else:
			if j == n:
				j = 0
			if i < 0:
				i = n - 1

		if magicSquare[int(i)][int(j)]: 
			j = j - 2
			i = i + 1
			continue
		else:
			magicSquare[int(i)][int(j)] = num
			num = num + 1

		j = j + 1
		i = i - 1 

	
	print("Magic Square for n =", n)
	print("Sum of each row or column", n * (n * n + 1) / 2, "\n")

	for i in range(0, n):
		for j in range(0, n):
			print('%2d ' % (magicSquare[i][j]), end='')
			if j == n - 1:
				print()

n = int(input("Introduce an odd number: "))
while n%2 == 0: 
  print("The number introduced is even!")
  n = int(input("Introduce an odd number: "))
generateSquare(n)
