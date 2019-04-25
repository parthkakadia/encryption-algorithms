while True:
	num = input("Enter: ")
	for i in range(100000):
		a=i*num
		if a%26==1:
				print i
				break
