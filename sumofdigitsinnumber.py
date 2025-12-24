def sumofnumber(n) :
    out = 0
    while n>0 :
        rem = n%10
        out = out + rem
        n = n//10
    return out
n = int(input("entr n :"))
print(sumofnumber(n))    