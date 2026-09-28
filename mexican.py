#Mexican -> Maxican Wave is a string technique in which one character at a time is changed to uppercase ,creating wave-like effect
def Mexican (n):
  length = len(n)
  for i in range(length):
    print(n[:i] + n[i].upper() + n[i+1:])


value =input("Enter a string :- ")
Mexican(value)