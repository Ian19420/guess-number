import random

start = eval(input('請決定隨機數字範圍開始值:'))
end = eval(input('請決定隨機數字範圍結束值:'))
r = random.randint(start, end)
count = 0
while True:
	count += 1
	num = eval(input('請猜數字:'))
	if num == r:
		print('你猜中了!')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print(f'這次你猜的第{count}次')
