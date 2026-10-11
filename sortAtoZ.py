# How to Sort the Disconary A to Z and Z to A.
data = {
  "mango":40,
  "aalu":10,
  "gobi":60,
  "palak":5
}
result=dict(sorted(data.items()))
print(result)

# Z to A Sorted

data2 ={
 
  "mango":40,
  "aalu":10,
  "gobi":60,
  "palak":5
}
des= dict(sorted(data2.items(),reverse=True))
print(des) 