#KAPREKAr no. => ek easa number hota hai jiska square karne ke baad us square ko do parts mein divide karne par ,un dono parts ka sum original number ke equal hota hai

def kaprekar(n):
  squar = n**2
  sum =0
  print("Square is",squar)
  while n>0:
    digit = len(str(squar))
    mid = digit//2
    left = int(str(squar)[:mid])
    right = int(str(squar)[mid:])
    print("the left side", left )
    print("the right side", right )

    sum = (left) + right
    print("sum", sum)
    if n==sum:
      return "It is a kaprekar number"
    else:
      return "It is not a kaprekar number"

value = int(input("Enter a number"))
print(kaprekar(value))  