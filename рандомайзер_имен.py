import random
import time

DELAY = 1.2
NAMES = ['ВВЕДИТЕ СВОИ ИМЕНА', 'ВВЕДИТЕ СВОИ ИМЕНА2', 'ВВЕДИТЕ СВОИ ИМЕНА3']
print('Рандомайзер выбирает...')
time.sleep(DELAY - 0.4)

def random_names():
    return random.choice(NAMES)

print(random_names())

lab = input('Хотите еще?(да/нет):')


if lab == 'да':
	print(random_names())
elif lab == 'нет':
	exit()	