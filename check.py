
list = ['TSLA', 'TESLA', 'WSB', 'TSLA', 'ACT', 'TSLA', 'AH', 'AMC', 'WSB', 'YOLO', 'TSLA', 'OK', 'US', 'GDP', 'TSLA']
new_list = []
n = 0


	
print (len(list))
for check in list:
	while n <= len(list):
		if check != new_list[n]:
			n +=1
		new_list.append(check)

