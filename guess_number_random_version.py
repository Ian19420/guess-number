def debug():
	for _ in range(100000):
		num = int(random.random()*99+1)
		if num > 99 or num < 1:
			print("there is a bug!")
			return False
		else:
			return True 
import random
num = int(random.random()*99+1)
x = debug()
if x:
	times = 0
	while 1:
		times += 1
		ans = eval(input("your guess(1~99)?:"))
		if ans == num:
			print("right!")
			print(f"you guessed {times} in total")
			break
		else:
			print("wrong!")
			if ans > num:
				print("answer is lower than your guess.")
			else:
				print("answer is higher than your guess.")
	else:
		print("error")


