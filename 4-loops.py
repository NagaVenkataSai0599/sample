#while loop

#implementing banking system
"""def checkBalance():
    return balance
def deposit():
    amount=int(input("Enter the amount to deposit:"))
    return amount
def withdraw():
    amount=int(input("Enter amount to be withdraw:"))
    return amount
balance=0
is_running=True
while is_running:
    print("Select any option from below(1-4)")
    print("1-checkbalance")
    print("2-deposit")
    print("3-withdraw")
    print("4-exit")
    ip=int(input())
    if ip==1:
        balance=checkBalance()
        print("Balance is:",balance)
    elif ip==2:
        balance+=deposit()
    elif ip==3:
        balance-=withdraw()
    elif ip==4:
        print("Thank You! visit again!")
        is_running=False
    else:
        print("Please enter an valid option")"""

#fizz buzz

"""num=1
end=int(input("Enter upto value:"))
while num<=end:
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    
    else:
        print(num)
    num+=1"""

#while loop to print first n even numbers or n odd numbers

'''i=1
count=0
choice=int(input("Enter your choice\n1-Even Numbers\n2-Odd Numbers"))
end=int(input("Enter how many numbers you want"))
while(count<end):
    if choice==1:
        if(i%2==0):
            print(i)
            count+=1
    elif choice==2:
        if(i%2!=0):
            print(i)
            count+=1
    i+=1'''
#print first n natural numbers
'''n=int(input("Enter a number:"))
sum=0
i=1
while(i<=n):
    sum+=i
    i+=1
print(f"Sum of first {n} natural numbers are:",sum)'''  
#multiplication tables 
'''num=int(input("Enter a table you want")) 
end=int(input("Enter how many steps you want"))
i=1
while(i<=end):
    print(f"{num}*{i}={num*i}")
    i+=1'''
#
