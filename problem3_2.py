from numpy import matrix
import math

def main(n = 10000000000):
	#mat = matrix('1,2,1; 1,0,0; 0,1,0', dtype = 'object') ** (n-1)
	if (n == 0):
		print(0)
	M = power(n-1) * matrix('2;1;0')
	print(M.item(1) % 10007)
	# ans = mat * matrix('2;1;0')
	# ans = ans.item(1)
	# print(ans)


def power(n):
	if (n == 0):
		return matrix('1,0,0; 0,1,0; 0,0,1', dtype = 'object')
	R = power(math.floor(n/2))
	R = R * R 
	if (n%2 == 1):
		R = R * matrix('1,2,1; 1,0,0; 0,1,0', dtype = 'object')
	return R % 10007

if __name__ == '__main__':
	main()


