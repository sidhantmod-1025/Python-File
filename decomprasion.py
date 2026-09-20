#Decomprasion 

s = input("Enter Compressed string : ")
i = 0 
result = ""

while i <len(s):
  ch = s[i]
  i=i+1

  num =""

  while i < len(s) and s[i].isdigit():
    num = num +s[i]
    i=i+1

  result = result + ch * int(num)  
print(result) 
