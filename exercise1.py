fin=open('brown.txt')
fout=open('output.txt','w')
lines=fin.readlines()
diction={}
n=4
for line in lines:
	words=line.split()

	for i in range(len(words)-n):
		key=words[i]+' '+words[i+1]+' '+words[i+2]+' '+words[i+3]
		if key not in diction:
			diction[key]=1
		else:
			diction[key]+=1
count=0
sum=0
for key in diction:
	outtxt=key,diction[key]
	fout.write(str(outtxt))
	fout.write('\n')
	if diction[key]<n:
		n=diction[key]
print('minimum:',n)

