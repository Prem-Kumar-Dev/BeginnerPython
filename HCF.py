def hcf(user):
	
	for i in range (2,min(user)+1):
		n=0
		
		while True:
			
			for x in (user):
				
				if x%i==0:
					n+=1
					
			if n == len(user):
					l=i
					break
			else:
					break
					
	print(l)


user_input=int(input('No. of values you want to work with:\n'))
lst=[]

for c in range(user_input):
	
	value=int(input('Enter the no.:\n'))
	lst.append(value)

hcf(lst)
