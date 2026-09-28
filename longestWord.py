text = "India is my country"

words = text.split()
longest = ""

for i in words:
    if len(i) > len(longest):
        longest = i

print(longest)