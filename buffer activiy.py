number = int(input("please enter any number"))
sum = 0
temp = number

while (temp > 0):
    factorial = 1
    i=1
    reminder = temp%10

    while(i<=reminder):
        factorial = factorial *1
        i=i+1
    
    print("\n factorial of %d = %d" %(reminder, factorial))
    sum = sum + factorial
    temp = temp // 10

print("\n sum of factorials of a given number %d = %d"%(number, sum))

if (sum == number):
    print("%d is a strong number" %number)
else:
    print("%d is not a strong number" %number)