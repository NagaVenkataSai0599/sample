#checking if a given number is even or odd
"""num=int(input("Enter a number:"))
if(num%2==0):
    print(f"{num} is an even Number")
else:
    print("{} is an odd number".format(num))"""

#checking greatest of three numbers aand equal numbers

'''n1=int(input("Enter number1:"))
n2=int(input("Enter number2:"))
n3=int(input("Enter number3:"))
if(n1>n2 and n1>n3):
    print(f"{n1} is greatest number among {n1,n2,n3}")
elif(n2>n1 and n2>n3 ):
    print(f"{n2} is greatest number among {n1,n2,n3}")
elif(n3>n1 and n3>n2):
    print(f"{n3} is greatest number among {n1,n2,n3}")
elif(n1==n2 and n1>n3):
    print(f"{n1} and {n2} are equal and they are greatest among {n1,n3}")
elif(n1==n3 and n1>n2):
    print(f"{n1} and {n3} are equal and they are greatest among {n1,n2}")
elif(n2==n3 and n2>n1):
    print(f"{n3} and {n2} are equal and they are greatest among {n1,n2}")
elif(n3==n1 and n1>n2):
    print(f"{n1} and {n3} are equal and they are greatest among {n2,n3}")
else:
    print(f"{n1},{n2},{n3} are equal")'''

#grading system:Create a program that takes a student's score as input and prints their grade based on the following criteria:

# A: 90 and above

# B: 80-89

# C: 70-79

# D: 60-69

# F: Below 60


"""score=int(input("Enter your Score:"))
if(score<0 or score>100):
    print("please enter score between 0-100")
elif(90<=score<=100):
    print("Your Grade is \"A\"")
elif(80<=score<=89):
    print("Your Grade is \"B\"")
elif(70<=score<=79):
    print("Your Grade is \"C\"")
elif(60<=score<=69):
    print("Your Grade is \"D\"")
else:
    print("Your are Failed,Better Luck Next Time!!!")"""

#checking whether the year is an leap year or not
"""year=int(input("Enter a year:"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(f"{year} is an leap year")
        else:
            print(f"{year} is not an leap year")
    else:
        print(f"{year} is an leap year")
else:
    print(f"{year} is not an leap year")"""

#Vowel or Consonant: Create a program that takes a single character as input and checks if it is a vowel or a consonant.
"""char=input("Enter a single character:")
vowels=['a','e','i','o','u','A','E','I','O','U']
if(char in vowels):
    print(f"{char} is vowel")
else:
    print(f"{char} is an consonant")"""

#Write a program that takes a number as input and prints whether the number is in the range 1 to 100 (inclusive).
'''num=int(input("Enter a number:"))
min=int(input("Enter Minimum value:"))
max=int(input("Enter Maximum value:"))
if(num>=min and num<=max):
    print(f"{num} is between the range from {min} to {max}")
else:
    print(f"{num} is out of the range from {min} to {max}")'''


#Write a program that checks if a given number is positive, negative, or zero
"""num=int(input("Enter a number:"))
if(num>0):
    print(f"{num} is an positive number")
elif(num<0):
    print(f"{num} is an negitive number")
else:
    print("Number is Zero")"""
#Write a program that takes a number as input and checks if it is divisible by both 3 and 5.
'''num=int(input("Enter a number:"))
if(num%3==0 and num%5==0):
    print(f"{num} is divisible by both 3 and 5")
else:
    print(f"{num} is not divisible by 3 and 5")'''

#Write a program that takes two numbers and an operator (+, -, *, /) as input and performs the corresponding arithmetic operation. Use conditional statements to handle the different operations.
'''n1=int(input("Enter number1:"))
n2=int(input("Enter number2:"))
op=input("Enter any operator between +,-,*,/,%,**,//:\n")
if(op=='+'):
    print(f"{n1}+{n2} = ",n1+n2)
elif(op=='-'):
    print(f"{n1}-{n2} = ",n1-n2)
elif(op=='*'):
    print(f"{n1}*{n2} = ",n1*n2)
elif(op=='/'):
    print(f"{n1}/{n2} = ",n1/n2)
elif(op=='%'):
    print(f"{n1}%{n2} = ",n1%n2)
elif(op=='**'):
    print(f"{n1}^{n2} = ",n1**n2)
elif(op=='//'):
    print(f"{n1}//{n2} = ",n1//n2)
else:
    print("Enter an valid operator")'''

#Write a program that takes the lengths of three sides of a triangle as input and determines whether the triangle is equilateral, isosceles, or scalene.
'''print("give the length of each side of an triangle")
s1=int(input("Enter 1st side length:"))
s2=int(input("Enter 2nd side length:"))
s3=int(input("Enter 3rd side length:"))
if(s1==s2==s3):
    print("It is an Equilateral treiangle")
elif(s1==s2 or s2==s3 or s1==s3):
    print("It is an isoceles treiangle")
else:
    print("It is an scalene triangle")'''

#Create a program that calculates the Body Mass Index (BMI) based on a person's height and weight and then categorizes the BMI result:

# Underweight: BMI < 18.5

# Normal weight: 18.5 <= BMI < 24.9

# Overweight: 25 <= BMI < 29.9

# Obesity: BMI >= 30

'''weight=float(input("Enter your weight in kg's:"))
height=float(input("Enter your height in meters:"))
bmi=weight/(height**2)
if(bmi<18.5):
    print(f"{bmi:.2f}=>UnderWeight")
elif(18.5<=bmi<24.9):
    print(f"{bmi:.2f}=>Normal Weight")
elif(25<=bmi<29.9):
    print(f"{bmi:.2f}=>OverWeight")
else:
    print(f"{bmi:.2f}=>Obesity")'''

#password strength checker


#nature of the roots of the quadratic equation
# If the discriminant is positive, there are two real and distinct roots.

# If the discriminant is zero, there is one real and repeated root.

# If the discriminant is negative, there are no real roots, but two complex roots.
'''import math
a=int(input("Enter the coefficient of x^2:"))
b=int(input("Enter the coefficient of x:"))
c=int(input("Enter the value for constant"))
print(f"The quadratice equation is:\n {a}x^2+({b})x+({c})")
dis=(b**2)-(4*a*c)
if(dis>0):
    r1=((-b)+math.sqrt(dis))/(2*a)
    r2=((-b)-math.sqrt(dis))/(2*a)
    print(f"The roots are {r1:.2f} and {r2:.2f}")
    print("Therefore the roots are real and distinct")
elif(dis<0):
    imgPart=math.sqrt(abs(dis))/(2*a)
    realPart=(-b/(2*a))
    r1=complex(realPart,imgPart)
    r2=complex(realPart,-imgPart)
    print(f"The roots are {r1} and {r2}")
    print("Therefore the roots are non-real and distinct roots")
else:
    r1=r2=-b/(2*a)
    print(f"The roots are {r1} and {r2}")
    print("The nature of the roots are real and equal")'''

#convert celcius to faherenheit and vice versa
"""ip=int(input("Enter\n1-celcius to fahereheit\n2-faherenheit to celcius\n"))
if(ip==1):
    cel=int(input("Enter celcius value:"))
    fh=((9/5)*cel)+32
    print(f"{cel}C is equal to {fh}F")
else:
    fh=int(input("Enter Faherenheit value:"))
    cel=(fh-32)*(5/9)
    print(f"{fh}F is equal to {cel}C")"""

#discount calculator
"""original_price=int(input("Enter amount:"))
discount=int(input("Enter the percentage of discount:"))
if(0<=discount<=100):
    #final_price=original_price-(original_price*(discount/100))
    final_price=original_price*((100-discount)/100)
    print(f"the actual price after taking {discount}% discount from {original_price} is {final_price}")
else:
    print("Please enter an valid discount percentage")"""
#to find the validity of an triangle
#The sum of any two sides must be greater than the third side.
#a+b>c
#a+c>b
#b+c>a
#If all three conditions are met, the sides can form a valid triangle. If even one of these conditions is not met, the sides cannot form a triangle.
'''s1=int(input("Enter side1:"))
s2=int(input("Enter side2:"))
s3=int(input("Enter side3:"))
if((s1+s2)>s3 and (s1+s3)>s2 and (s2+s3)>s1):
    print("It is an valid triangle")
else:
    print("it is an invalid triangle")'''
#check the given string is palindrome or not
'''str=input("Enter a string:")
for i in range(len(str)-1,0):'''





    






        


