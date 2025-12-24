def rev(n) :
    out=0
    while n>0 :
        rem = n%10
        out = out*10+rem
        n = n//10
    return out
n = int(input("enter no :"))
print(rev(n))

