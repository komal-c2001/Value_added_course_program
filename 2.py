n = int(input("Enter a numeber="))
flag = 0
for i in range(2,n):
    if(n % i == 0):
        flag = 1
        break
if(flag == 0):
    print("Given number is prime number")
else:
    print("Given number is not prime number")
