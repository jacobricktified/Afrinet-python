#use try catch to handle exception
try:
    num=int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input! Please enter a valid integer.")