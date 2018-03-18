# Digital Root

 # The digital root (also repeated digital sum) of a non-negative integer is the (single digit) 
 # value obtained by an iterative process of summing digits, on each iteration using the result 
 # from the previous iteration to compute a digit sum. The process continues until a single-digit 
 # number is reached.

 ## Example Outputs

 # Given you have a method or a function called `dr`, the following should be true:


def dr(number):
# last digit + rest of the number
	if number < 10:
		return number

	while number >= 10:
		remainder = number % 10 # 8, 5
		number = number // 10 # 7, 1
		sum_ = number + remainder # 15, 6
		if sum_ >= 10: 
			number = sum_ # 15

	return sum_


def dr_recursive(number):
	# number = 78
	if number < 10:
		return number
	remainder = number % 10 # 8, 5
	rest = number // 10 # 7, 1
	return dr_recursive(rest + remainder)


print(dr_recursive(0) == 0)
print(dr_recursive(1) == 1)
print(dr_recursive(9) == 9)
print(dr_recursive(10) == 1)
# print("dr 78: ", dr(78))
print(dr_recursive(78) == 6)
print(dr_recursive(100) == 1)
print(dr_recursive(142) == 7)
print(dr_recursive(1424) == 2)
print(dr_recursive(56734) == 7)
print(dr_recursive(967335) == 6)
print(dr_recursive(95395367335) == 4)



