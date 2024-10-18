# student_scores =input("input a list of student scores ").split(",")
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 78,65,89,86,55,91,64,89
# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
# print(f"The higest score in thefor number in range (1, 11, 3):
#     print (number) class:  {max_score}")


# Try replicating this max function to for loop
# print(max(student_scores))



# for loops and the range()function
# so far we hv been coding with for loop when it is associated with list but sometimes we might want to use loop completely independent of a list

# For Loop with Range
# for number in range(1, 11, 3):
#     print(number)

# to use range-u want to generate a range of numbers to loop through
# range function looks like this:

# for number in range(a, b):
#     print(number)

# for examples:
# for number in range(1, 10):
#     print (number)

# # this will output all the number from 1 to 9 excluding 10

# # if u want to including 10:
# for number in range (1, 11):
#     print(number)

# in this range increases by 1
# if u want it to be increased by any number else that is not 1,it should be done like this:

# for number in range (1, 11, 3):
#     print (number)

# it will  give 1,4,7,10 increasing in 3 steps
#  it will  give 1,3,5,7,9 increasing in 2 steps

# to add together number 1 to 100:

total =0
for number in range (1, 101):
    total += number
print(total)
    



