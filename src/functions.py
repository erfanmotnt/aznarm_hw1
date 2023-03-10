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

def correct_division2(a, b):
	return a // b
	
def calculator(a, b, action):
	if action is 'sum2':
		return sum2(a, b)
	elif action is 'minus2':
		return minus2(a, b)
	elif action is 'multiply2':
		return multiply2(a, b)
	elif action is 'division2':
		return division2(a, b)
	elif action is 'remaining':
		return remaining(a, b)
	else:
		raise 'Error: bad request'
	