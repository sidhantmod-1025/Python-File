num = "123456789"

length = len(num)

for i in range(length):
    print(num[i],end="")

    if (length - i - 1) % 3 == 0 and i != length - 1:
        print(",",end="")