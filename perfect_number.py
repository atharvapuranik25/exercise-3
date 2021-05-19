N_int=int(input("Numbers to be validated: ")) # Number to be validated
Div=1    #Divisor
num=2
while num<N_int+1:
    sum=0
    #This stores the sum of divisors and reverts back to 0 when we get a new num
    while Div<num:
        if num % Div==0:
            sum=sum+Div
        Div=Div+1
    if num==sum:
        print(num, "is perfect")
    elif num<sum:
        print(num, "is abundant")
    else:
        print(num, "is deficient")
    Div=1
    num=num+1
