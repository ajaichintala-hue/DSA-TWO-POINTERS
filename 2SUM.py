# DSA-TWO-POINTERS
BASIC DSA QUETIONS BY USING 2 POINTERS METHOD

def two_sum(number):
  s={}
  target=9
  for i in range(0,len(number)):
    remaining=target-n[i]
    if remaining in s:
      return[s[remaining],i]
    else:
      s[n[i]]=i
n=[2,7,8,11]
two_sum(n)
