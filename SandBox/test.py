def gcd(num1, num2):
    while num2:           #! Continue loop until num2 becomes zero
        num1, num2 = num2, num1 % num2 #* Swap num1 with num2, and num2 with the remainder of num1 divided by num2
    return num1         #* When num2 becomes zero, num1 is the GCD

print("Output:", gcd(24,32))