fp = open("test1.html",'r')
l = fp.readlines()
fp.close()

l1 = len(l)

fp = open("test2.html",'w')
fp.close()

i = 0
l4 = []
#for i in range(l1):
while i < (l1-1):
	f = 0
	day = 0
	start = 0
	end = 0
	if('<table border="3" style="width:100">' in l[i]):
		for j in range(i,l1):	
			if('<td bgcolor="#98AFC7"><b>' in l[j]):
				for k in range(j+1,l1):
					#print(l[k])
					#print(k)
					if('<td>0/0</td>' in l[k]):
						day = day+1
						#print("First Break")
						break
					if('<td bgcolor="#98AFC7"><b>' in l[k]):
						f = 1
						#print("Second Break")
						#print(k)
						break
			if(f == 1):
				#print("Third Break")
				break
			if(day == 5):
				start = i
				for m in range(k,l1):
					if('<table border="3" style="width:100">' in l[m]):
						end = m-1
						break
				#print(start)
				#print(end)
				print(l[i-1])
				l4.append(l[i-1])
				#print("Fourth Break")
				break
	if(start !=0):
		fp = open("test2.html",'r')
		l2 = fp.readlines()
		fp.close()
			
		l3 = len(l2) - 1
		fp = open("test2.html",'w')
		fp.close()
			
		for j in range(l3):
			if(l2[j] != l[i-1]):
				fp = open("test2.html",'a')
				fp.writelines(l2[j])
				fp.close()
		i = end

		print("2222222222",i)
	else:
		fp = open("test2.html",'a')
		fp.writelines(l[i])
		fp.close()	
		i = i + 1
	
	
print(l4)

