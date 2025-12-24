def rev(n):
    a = n  
    out = 0
    while n > 0:
        rem = n % 10
        out = out * 10 + rem
        n = n // 10
    
    if a == out:
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")

number = int(input("Enter a number: "))
rev(number)

    