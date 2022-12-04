 
import random

def guess(x):
	random_number = random.randint(1, x)
	guess = 0
	while guess != random_number:
		guess = int(input('Chute um número entre 1 e {x}'))
		if guess < random_number:
			print('Desculpa, chute novamente. Muito baixo.')
		elif guess > random_number:
			print('Desculpa, chute novamente. Muito alto.')

	print('Uhulll, parabéns. O número era: {random_number} e você acertou!!')

def computer_guess(x):
	low = 1
	high = x
	feedback = ''
	while feedback != 'c':
		if low != high:
			guess = random.randint(low, high)
		else:
			guess = low
		feedback = input(f'O número {guess} é muito alto (A), muito baixo (B) ou correto (C)??').lower()
		if feedback == 'a':
			high = guess - 1
		elif feedback == 'b':
			low = guess + 1

	print(f'Uhulll! O número era {guess}, e o computador acertou!!')

uess(100)