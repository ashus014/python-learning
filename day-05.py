england_clubs = ["Liverpool", "Newcastle United", "West Ham United", "Ashton Villa"]

# for club in england_clubs:
#     print(club)
#     print(club + " is a winner")

# for loop with range
# end_range = int(input("What is the end range : "))
# for number in range(1,11):
#     print(number)

# for number in range(2,11,2):
#     print(number)

# total = 0
# for i in range(2,101,2):
#     total += i
# print(total)

# Fizz Buzz coding exercise
number = 15
for i in range(1,number+1):
    if i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


