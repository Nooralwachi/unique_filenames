def unique_filenames(input):
	output= {}
	for item in input:
		flag = True
		while(flag):
			if item not in output:
				output[item] = 0
				flag = False
			else:
				value = output[item]
				newname = item +'(' + str(value +1) + ')' 
				if newname not in output:
					output[newname] = 0
					flag = False
				else:
					output[item] +=1
	for key in output.keys():
		print (key)

unique_filenames(["pes","fifa","gta","pes(2019)"])
print("---------------------")
unique_filenames(["gta","gta(1)","gta","avalon"])
print("---------------------")
unique_filenames(["kaido","kaido(1)","kaido","kaido(1)"])