driving = input('請問你有沒有開過車？')
age = input('請問你的年齡: ')
age = int(age)
if driving == '有':
	if age < 18:
		print('你壞壞，不可以')
	else:
		print('ok 沒問題')
elif driving == '沒有':
	if age > 18:
		print('快去考駕照')
	else:
		print('你還小，慢慢等')
else:
	print('請回答有或沒有！！')