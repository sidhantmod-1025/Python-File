num = "818288187828"
length=len(num);

sum=0
for i in range(length):
  if(num[i]=="8"):
   
    sum=sum+1
    if i>0: 
     if(num[i-1]=="8"):
      sum=sum+2
  print("the sum",sum)





 