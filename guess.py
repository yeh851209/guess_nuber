import random
max = input('請輸入最大值')
min = input('請輸入最小值')
max = int(max)
min = int(min)
r = random.randint(min, max)
x = 0
while True :
	x =x + 1
	guest = input('請輸入數字')
	guest = int(guest)
	if guest == r :
		print('恭喜你猜到了')
		break
	elif guest >= max :
		print('清輸入介於',min,'和',max,'之間')
	elif guest <= min :
		print('清輸入介於',min,'和',max,'之間')
	elif guest < r :
		min = guest
		print('數字介於',min,'和',max,'之間')
	elif guest > r :
		max = guest
		print('數字介於',min,'和',max,'之間')


