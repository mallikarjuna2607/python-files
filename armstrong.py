t = int(input("Enter number of test cases: "))
for _ in range(t):
    n = int(input("Enter input: "))
    temp = n
    num_digits = len(str(n))
    total = 0
    
    while temp > 0:
        digit = temp % 10
        total = total + digit ** num_digits
        temp //= 10
    
    if total == n:
        print("Yes - Armstrong")
    else:
        print("Not - Armstrong")
