
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

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age ? "))
    if age < 12:
        print("Please pay $5.")
    elif age <=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("sorry you can't ride")