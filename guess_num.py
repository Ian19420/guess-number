import random
r = random.randint(1, 100)
while True:
	num = eval(input('請猜數字:'))
	if num == r:
		print('你猜中了!')
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
