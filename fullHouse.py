list = ["p","s","A","K"]
if len(list) != 5:
    print("Not Full House")
    exit()
valid_List = [
  "A","2","3","4","5","6","7",
  "8",
  "9",
  "10",
  "j",
  "k",
  "Q"
]
for a in list:
    if a not in valid_List:
        print("Invalid card")
        exit()

three = False
two = False
for a in list :
  count =list.count(a)

  if count == 3:
    three = True
  if count == 2:
    two = True 
if three and two:
  print("Full House ") 
else :
  print("Print not a full house")     