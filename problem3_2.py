from numpy import matrix
import math

def main():
	# grab the input value 
	n = input()
	if (n == 0):
		print(0)

	M = power(n-1) * matrix('2;1;0')
	print(M.item(1) % 10007)


def power(n):
	# stopping condition 
	if (n == 0):
		return matrix('1,0,0; 0,1,0; 0,0,1', dtype = 'object')

	R = power(math.floor(n/2))
	R = R * R 

	if (n % 2 == 1):
		# the matrix is specific to our series' defination
		R = R * matrix('1,2,1; 1,0,0; 0,1,0', dtype = 'object')
	# get the mod of the matrix at every iteration so that the snumber
	# dont get too big for calulations 
	return R % 10007

if __name__ == '__main__':
	main()


