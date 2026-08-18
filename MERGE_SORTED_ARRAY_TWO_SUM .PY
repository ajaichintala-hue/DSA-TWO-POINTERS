#MERGE SORTED ARRAY TWO SUM 

def two_sum(number):
  s={}
  target=9
  for i in range(0,len(number)):
    remaining=target-n[i]
    if remaining in s:
      return[s[remaining],i+1]
    else:
      s[n[i]]=i+1
n=[2,7,8,11]
two_sum(n)
