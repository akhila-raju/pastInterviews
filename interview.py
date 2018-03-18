


def xyz(string):
	string = string.split(" ")
	# [4 2 3 3 / * /]
	index = 0
	# for index in range(len(string))
	while index < len(string):
		# if index > len(string)-1:
		# 	index = len(string) - 1
		if string[index] == "+":
			curr = int(string[index-1]) + int(string[index-2])
			string = string[:index-2] + [curr] + string[index+1:]
			index = index-2
		elif string[index] == "/":
			curr = int(string[index-2]) / int(string[index-1]) 
			string = string[:index-2] + [curr] + string[index+1:]
			# [4 2 1 * /]
			# update index to index - 1
			index = index-2
		elif string[index] == "*":
			curr = int(string[index-1]) * int(string[index-2]) 
			string = string[:index-2] + [curr] + string[index+1:]
			index = index-2
		index += 1

	return string[0]

	# 


print(xyz("3 3 +"))
print(xyz("2 2 + 3 *"))
print(xyz("2 2 3 + *") )
print(xyz("4 2 3 3 / * /"))