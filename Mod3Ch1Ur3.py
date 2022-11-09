num = int(input('Введите число '))
a = 0
while (num>0):
	a=a+num%10
	num//=10
	
print(a)
