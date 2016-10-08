s = input("Enter a number: ")
#number = float(s)
try:
	number = float(s)
except:
	number = 0
answer = number * number
print(number,"*",number,"=",answer)