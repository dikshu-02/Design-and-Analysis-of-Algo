from math import floor, ceil

def karatsuba(x,y):
    if (len(str(x))<=1 or len(str(y))<=1):
        return x*y
    n_=max(len(str(x)),len(str(y)))
    n=ceil(n_/2)
    a=floor(x/(10**n))
    b=floor(x%(10**n))
    c=floor(y/(10**n))
    d=floor(y%(10**n))
    ac=karatsuba(a,c)
    bd=karatsuba(b,d)
    ad_plus_bc=karatsuba((a+b),(c+d))-ac-bd
    prod=(ac* 10**(2*n)) + (ad_plus_bc *10**n) + bd
    return prod
    

num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
result=karatsuba(num1,num2)
print("The solution is ",result)
