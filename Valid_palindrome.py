#checking the valid palindrome or not 
s="A man, a plan, a canal: panama"
left=0
right=len(s)-1
while left<right:
  if not s[left].isalnum():
      left=left+1
  elif not s[right].isalnum():
      right=right-1
  elif s[left].lower()!=s[right].lower():
      print("not palindrome")
  else:
      left=left+1
      right=right-1
print("palindrome")
    
    
