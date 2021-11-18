fin=open('brown.txt')
fout=open('output.txt','w')
lines=fin.readlines()
diction={}
min=None
for line in lines:
	words=line.split()

	for i in range(len(words)-4):
		key=words[i]+' '+words[i+1]+' '+words[i+2]+' '+words[i+3]
		if key not in diction:
			diction[key]=1
		else:
			diction[key]+=1

for key in diction:
	outtxt=key,diction[key]
	fout.write(str(outtxt))
	fout.write('\n')
	if min is None or diction[key]<min:
			min=diction[key]
print('minimum:',min)

