#MOVING ALL ZEROS TO RIGHT SIDE USING 2 POINTERS

n=[0,1,0,3,12,0]
l=0
r=1
while r<len(n)-1:
  if n[l]==0:
    temp=n[l]
    n[l]=n[r]
    n[r]=temp
    l=l+1
    r=r+1
  if n[r]==0:
    r=r+1
print(n)
