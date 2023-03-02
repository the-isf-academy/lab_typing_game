from prompts import prompt_list
from random import choice
from helpers import print_slow, calculate_wpm, calculate_accuracy, generate_prompt
from time import time

####  Welcome Screen

print("-"*50)
print("Welcome to the ISF Typing Game")
print("-"*50)

#### Game Rules

user_start = input("> Input any key to view the rules.")

print("     1. You will see the prompt")
print("     2. The timer will start")
print("     3. Type the prompt as fast as you can")
print("     4. Click 'enter/return' when you are done.\n")

#### Game Start Countdown
user_start = input("> Input any key to start the game! ")

print("-"*30)
print("The game will start in...")
print_slow("3...2...1!", .2)
print("-"*30,"\n")


#### 💻 YOUR CODE GOES HERE 💻 ####


chosen_prompt = choice(prompt_list)        # store a single prompt
#chosen_prompt = generate_prompt()
print(chosen_prompt)                       # print prompt

start_time = time()                 # start timer

user_typed_prompt = input(">>> ")     # get user input

end_time = time()                   # end timer

user_wpm = calculate_wpm(user_typed_prompt, start_time, end_time) #calculate wpm
user_accuracy = calculate_accuracy(chosen_prompt, user_typed_prompt)

print("-"*30,'\n')

print("WPM: {}".format(user_wpm))            # print statistics for user
print("Accuracy: {}%".format(user_accuracy*100))
