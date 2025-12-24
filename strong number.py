def strnum(n) :
    total = 0
    a =n 
    while n>0 :
        rem = n%10
        fact = 1
        while rem > 0 :
            fact = fact*rem
            rem-=1
        total = total + fact
        n = n//10
    if a == total :
        return " strong Number"
    else :
        return " NOt strong"
n = int(input("entr N :"))
print(strnum(n))