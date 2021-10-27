# 密码验证程式
# 先在程式码中，设定好密码 password = 'a123456'
# 让使用者【最多输入3次密码】
# 不对的话，就印出【密码错误！还有__次机会】
# 对的话，就印出【登入成功】

password = 'a123456' # 设置正确密码
user_try = 3 # 设置用户最大尝试次数

while True:
	user_password = input('请输入密码： ')
	if user_password == password: # 如果用户密码输入正确，程序终止
		print('登入成功！')
		break
	else:
		user_try -= 1 # 如果用户输入错误，用户尝试次数减一
		print(f'密码错误！还有{user_try}次机会。')
		if user_try == 0: # 如果用户输入三次错误，程序终止
			print('请重新设置密码！')
			break