ngk11,ngk21=list(map(int,input().split()))
lt1=list(map(int,input().split()))
lt2=[]
while(ngk21):
	gm = list(map(int,input().split()))
	lt2.append(gm)
	ngk21-=1
for icc in lt2:
	v=0
	for jcc in range(icc[0]-1,icc[1]):
		v=v^lt1[jcc]
	print(v)
