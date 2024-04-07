# Egyptian Multiplication

ans = []
while True:
    try:   
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input")
while (a >= 1 and a > 0) or (a <= -1 and a < 0):
    if (a % 2 != 0 and a > 0):
        ans.append(b)
        print(f"add {b}")
    elif (a % 2 != 0 and a < 0):
        ans.append(-b)
        print(f"add {-b}")
    a //= 2
    b *= 2
print(f"Answer: {sum(ans)}")