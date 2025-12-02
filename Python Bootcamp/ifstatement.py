num1=2
if num1==2:
    print("true")
elif num1 ==0:
    print ("this is zero")
else:
    print("false")

num2=10
if num2==10:
    print("you are number 10 ")
else:
    print("you are not number 10")
age =input("Enter your age: ")
age = int(age)
if age >=18:
    print("you are an adult")
elif age <18 and age >0:
    print("you are a minor")
else:
    print("Age not identified")
    
num3 = input("Enter first number: ")
num4 = input("Enter second number: ")   
num3 = int(num3)
num4 = int(num4)
sum_numbers = num3 + num4
if sum_numbers > 20:
    print("The sum is greater than 20")
else:
    print("The sum is not greater than 20") 
