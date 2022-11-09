x = float(input())
p = float(input())
y = float(input())
a = 0
while x<y:
	x*=1+p/100
	x=int(100*x)/100
	a+=1
print(a)