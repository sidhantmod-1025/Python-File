def vowels(n):
  count =0
  length = len(n);
  for i in range(length):
    if(n[i].lower() in"aeiou"):
      count =count+1;

  print(count)

text = input("Enter a Sring :- ")  
vowels(text)