country = input('country?')
age = int(input('age?'))
if country == 'Taiwan':
	if age >= 18:
		print('you can drive')
	else:
		print('you cannot drive')

elif country == 'America':
	if age >= 16:
		print('you can drive')
	else:
		print('you cannot drive')

else:
	print('please enter Taiwan or America only')
