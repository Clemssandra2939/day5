student_scores =input("input a list of student scores ").split(",")
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 78,65,89,86,55,91,64,89
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(f"The higest score in the class:  {max_score}")


# Try replicating this max function to for loop
# print(max(student_scores))



# for loops and the range()function
so far we hv been coding with for loop when it is associa