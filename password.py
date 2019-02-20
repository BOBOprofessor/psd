x = 3
while True :
	p = input('請輸入密碼')
	if p == 'yoyo21335':
		print('登入成功') 
		break
	elif p != 'yoyo21335':
		x = x - 1
		print('你還剩', x,'次機會')
		if x == 0:
			break


