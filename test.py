name = ''
while name != 'Joe':
	print('Who are you?')
	name = input()
	if name == 'Joe':
		print('Hello Joe. What is the password?')
		password = input()
		while (password != 'swordfish'):
			print('Hello Joe. What is the password?')
			password = input()
print('Access granted.')