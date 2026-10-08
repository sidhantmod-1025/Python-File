l=[2,4,3,"sidhant",True]
print(l);
print(type(l))

l.append(6);
print(l)
l.reverse()
print("reverse",l)
#l.sort()
#print("sort",l)
print(l[3])
print(l[2])  
print(len(l)-3) #negative indixing

if "dha"in "sidhant":
  print("yes")

print(l[:])