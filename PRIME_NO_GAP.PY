#CONSECUTIVE PRIME NUMEBER HIGH GAP UNDER RANGE
l=[]
n=int(input("enter range :"))
for i in range(2,n):
    p=i
    x=True
    for j in range(2,i):
        if i%j==0:
            x=False
            break
    if x:
       l.append(i)
left=0
right=1
maxgap=0
while right<len(l) and left<len(l)-1:
    curgap=l[right]-l[left]
    maxgap=max(curgap,maxgap)
    left=left+1
    right=right+1
for i in range(0,len(l)-1):
    if l[i+1]-l[i]==maxgap:
        print(maxgap,"and",l[i],"between",l[i+1])
        break
