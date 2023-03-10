def sum2(a, b):
	return a + b

def minus2(a, b):
	return a - b

def multiply2(a, b):
	return a * b

def division2(a, b):
	return a / b

def remaining(a, b):
	return a % b

def calculator(a, b, action):
	if action == 'sum2':
		return sum2(a, b)
	elif action == 'minus2':
		return minus2(a, b)
	elif action == 'multiply2':
		return multiply2(a, b)
	elif action == 'division2':
		return division2(a, b)
	elif action == 'remaining':
		return remaining(a, b)
	else:
		raise 'Error: bad request'
	