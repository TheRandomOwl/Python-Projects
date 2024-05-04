def egyptian_multiplication(a, b):
    ans = []
    while abs(a) >= 1 and abs(a) > 0:
        if (a % 2 != 0 and a > 0):
            ans.append(b)
        elif (a % 2 != 0 and a < 0):
            ans.append(-b)
        print(f"halve {a}, double {b}")
        a = int(a/2)
        b *= 2
    print(f"add {[abs(num) for num in ans]}")
    print(f"Answer: {sum(ans)}")

def main():
    egyptian_multiplication(-12, 5)

if __name__ == "__main__":
    main()
