state_of_Nigeria =["Abia","Adamawa","Anambra","Enugu","Imo","Kaduna","Abuja","Kano","Lagos","Niger","Edo","Cross River","Bauchi","Ebonyi"]

# for state in state_of_Nigeria:
#     print(state + " state")

first_state = state_of_Nigeria[0].split(",")
print(state_of_Nigeria)

# split() is used to seperate and make  a string into a list automatically
# split(",")

# sum()-to add up number
# max() - to pick the highest number
# min()-to pick lowest number
# len() to count the number of items



# Head or tail coin coding exercise
# import random 
# test_seed=int(input("create a seed number "))

# random.seed(test_seed)

# random_side=random.randint(0,1)
# if random_side==1:
#     print("Heads")

# else:
#     print==("Tails")

# ROck,Paper,Scissor
import random
Rock =''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper ='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
gaming_images =[Rock,Paper,Scissor]


my_choice=int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors:\n"))

print(gaming_images[my_choice])

computer_choicee=random.randint(0,2)
print("Computer`s choice is:")

print(gaming_images[computer_choicee])


if my_choice >= 3 or my_choice < 0:
    print("You added an invalid number! Try again")
elif my_choice == 0 and computer_choicee == 2:
    print("You win!")
elif computer_choicee == 0 and my_choice == 2:
    print("You lose!")
elif computer_choicee > my_choice:
    print("You lose!")
elif my_choice > computer_choicee:
    print("You win!")
elif my_choice == computer_choicee:
    print("it is a draw!")




import random
test_seed =int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names,separated by a comma:")
names = namesAsCSV.split(",")

# Get the total number of items in list
num_items= len(names)
# generate random number between 0 and the last number
random_names =random.randint(0,num_items - 1)
person_who_will_pay =names[random_names]

print(person_who_will_pay +"  is going to buy the meal today!")