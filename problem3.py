import sys
def main():
	print(sys.getrecursionlimit())
	n = int(input('Enter value of n'))
	mem = dict()
	Fn = find(mem,n)
	print(Fn)
	print(Fn % 10007)


def find(mem,n):

	if n in mem:
		return mem[n]
	else:
		if(n <= 2):
			mem[n] = n
			return mem[n]

		else:
			mem[n] = find(mem,n-3) + (2 * find(mem,n-2)) + find(mem,n-1)
			return mem[n]

if __name__ == '__main__':
	main()