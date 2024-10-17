# # Using loops with python lists

# # For Loops(can be used for item in list of items) 

# fruits = ["Apples","Peach","Pear","Banana"]
# for fruit in fruits:
#     print(fruit)
    
# # fruit as  variable to the items in fruits
# # loops always us to excute the same line of code muitiple times
# print(fruit + "Pie")
# # this is + pie is adding pie in all of the items in the list



# Average Height Exercise coding char
student_heights = input("input a list of student heights ").split(",")
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height=0
for height in student_heights:
    total_height += height
print(total_height)
# 156,178,165,171,187

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

average = round(total_height/number_of_students)
print(average)

# total_height= sum(student_heights)
# number_of_students=len(student_heights)
# average_height= round(total_height/ number_of_students)
# print(average_height)
