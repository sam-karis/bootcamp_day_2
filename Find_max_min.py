def find_max_min(num_list):
	maximum = num_list[0]
	minmum =num_list[0]
	for num in num_list:
		if maximum < num:
			maximum = num
		elif minmum > num:
				minmum = num
	res =  [minmum, maximum]
	if minmum == maximum:
		return [len(num_list)]
	else:
		return res

print (find_max_min([ 66, 1, 6, 44, 7, 78, 8, 68, 2]))