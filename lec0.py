l = list(input())
flag = True
if flag:
  flag = False
  for i in range(len(l) - 1):
    if l[i] > l[i+1]:
      flag = True
      l[i],l[i+1] = l[i+1],l[i]
return l       
    
