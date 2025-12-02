#nested if statement of age and have an id card
age = input("Enter your age: ")
age = int(age)
if age >=18:
    has_id_card = True
    if has_id_card:
        print("You are allowed to enter the club")
    else:
        print("You need an ID card to enter the club")  
