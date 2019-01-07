print("Comparison sorting program!")

data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]

print("Number of elements to sort:",len(data))

for scanIndex in range(0,len(data)):
	minIndex = scanIndex

	for compIndex in range(scanIndex+1,len(data)):
		if data[compIndex] < data[minIndex]:
			minIndex = compIndex

	if minIndex != scanIndex:
		# If the instruction is long, it can be 
		# moved to the next line with backslash "\"
		# which have to be the last character in the string
		# even spaces not allowed
		data[scanIndex],data[minIndex] = \
		data[minIndex],data[scanIndex]
		print(data)