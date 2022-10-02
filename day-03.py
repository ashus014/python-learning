
###########   Day 3 Learning

# print(" :: Welcome :: ")
# height = int(input("What is your height in cm ?"))

# if height > 120:
#     print("You can ride the rollercoaster")
# else:
#     print("sorry you can't ride")

print(7%3)

#nested if-else statement
print(" :: Welcome :: ")
height = int(input("What is your height in cm ?"))
bill = 0

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age ? "))
    if age < 12:
        bill = 5
    elif age <=18:
        bill = 7
    else:
        bill = 12
    
    wants_photo = input("Do you want your photo takne ? (Y/N) : ")
    if wants_photo == "Y" or wants_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}.")

else:
    print("sorry you can't ride")