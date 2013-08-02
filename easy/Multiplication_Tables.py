for i in range (1, 13):
	list = [str('%d'.rjust(4 - len(str(i))) % (i))]
	for j in range (2, 13):
		list.append(str('%d'.rjust(6 - len(str(i * j))) % (i * j)))
	print ''.join(list)
		
	