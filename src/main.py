from functions import sum2

if __name__ == '__main__':
	inp = input("enter action:")
	a, b = inp.strip().split(' ')
	a, b = int(a), int(b)
	s = sum2(a, b)
	print(s)
