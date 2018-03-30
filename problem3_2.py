import math
class matrix():
	''' The class has all the needed methods for calculating the fibonachi number'''

	# creating matrix class and defining dunder methods to perform 
	# matrix multiplication and matrix mod and item
	def __init__(self, data):
		self.mat = data

	def __mul__(self, obj):
		m1 = self.mat
		m2 = obj.mat
		
		self.ans = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]
		for i in range(len(m1)):
			for j in range(len(m2[0])):
				for k in range(len(m2)):
					self.ans[i][j] += m1[i][k] * m2[k][j]
		return matrix(self.ans)

	def __mod__(self, obj):
		for i in range(len(self.mat)):
			for j in range(len(self.mat[0])):
				self.mat[i][j] = self.mat[i][j] % obj
		return matrix(self.mat)

	def item(self, index):
		i = index // len(self.mat[0])
		j = index % len(self.mat[0])
		return self.mat[i][j]

	def __repr__(self):
		return 'Pranav-Matrix: {}'.format(self.mat)

def main(): 
	n = int(input())
	if (n == 0):
		print(0)
	M = power(n-1) * matrix([[2],[1],[0]])
	print(M.item(1)% 10007)

def power(n):
	# stopping condition 
	if (n == 0):
		return matrix([[1,0,0],[0,1,0],[0,0,1]])

	R = power(math.floor(n/2))
	R = R * R

	if (n % 2 == 1):
		# the matrix is specific to our series' defination
		R = R * matrix([[1,2,1],[1,0,0],[0,1,0]])
	# get the mod of the matrix at every iteration so that the snumber
	# dont get too big for calulations 
	return R % 10007
 

if __name__ == '__main__':
	main()


