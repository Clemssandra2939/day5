# Adding even  number from 1 to 100 including 1 and 100

# total_numbr = 0
# for numbr in range (2, 101,2):
#     total_numbr += numbr
# print(total_numbr)


# total_number = 0
# for number in range (1,101):
#     if number % 2==0:
#         total_number += number
# print(total_number)



# Fizz Buzz coding char
# You are going to write a program that automatically print the solution
# to the fizz buzz game

# Your program should print each number fro 1 to 100 in turn
# when the number is divided by 3 then instead of printing the number,it should print "fizz"
#  when the number is divided by 5 then instead of printing the number,it should print "buzz"
# And if the number is divided by 3 and 5 instead of printing the number,it should print "Fizz Buzz"


for num in range (1,101):
    if num % 3 == 0 and num % 5 ==0:
        print("FizzBuzz")
    elif num % 3 ==0:
        print("Fizz")
    elif num % 5 ==0:
        print("Buzz")
    else:
        print(num)
    
    