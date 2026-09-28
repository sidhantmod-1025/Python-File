def BackWord(n):
  word = n.split()
  final= word[::- 1]
  print(final)

text = "India is my country"
BackWord(text)  