# Name Guessing Game
# Program will continuously loop until the correct name is entered

print("You have to enter a list of random names until you guess the correct name ".upper(), "\n")
name_list = []
incorrect_names = []
input("Type in 'Yes' to begin ! :  ")
user_name_input = str()
correct_name = "John"
print("Hint.. The correct name has 4 letters and starts with the letter 'J' \n")

while user_name_input != correct_name:
    incorrect_names = name_list.append(user_name_input)
    user_name_input = input("Enter a random name : ")
    if user_name_input == correct_name:
        break
# By applying the break control, the loop will be terminated once the user enters the correct name
print(name_list)
