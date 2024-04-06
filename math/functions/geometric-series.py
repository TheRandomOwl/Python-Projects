N = 100 #int(input("Enter a N value: "))
n = int(input("Enter starting index: "))
a = float(input("Enter value for a: "))
r = float(input("Enter a value for r: "))

ans = a*(r**n)
for k in range(n+1,N):
    ans += a*(r**k)

print(ans)