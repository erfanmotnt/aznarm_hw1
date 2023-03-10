from functions import calculator

if __name__ == '__main__':
	inp = input("enter action:")
	while inp is not 'end':
		action, a, b = inp.strip().split(' ')
		a, b = int(a), int(b)
		print(calculator(a, b, action))
		inp = input("enter action:")
