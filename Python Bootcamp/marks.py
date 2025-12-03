#ask user to enter marks from kyboard if marks 0-20 print fail 21-40 that is a e 41-60 print good tryal 81-100 excellent 61-80 very good 
marks = input("Enter yor marks:")
marks = int(marks)
if marks >=0 and marks <=20:
    print("Fail")   
elif marks >=21 and marks <=40:
    print("E")  
elif marks >=41 and marks <=60:
    print("Good trial") 
elif marks >=61 and marks <=80:
    print("Very good")
elif marks >=81 and marks <=100:
    print("Excellent")      
else:
    print("Invalid marks")  