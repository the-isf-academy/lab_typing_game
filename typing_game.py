from prompts import prompt_list
from random import choice
from helpers import print_slow, calculate_wpm, calculate_accuracy, generate_prompt
from time import time

####  Welcome Screen

print("-"*50)
print("Welcome to the ISF Typing Game")
print("-"*50)

#### Game Rules

input("> Input any key to view the rules.")

print("     1. You will see the prompt")
print("     2. The timer will start")
print("     3. Type the prompt as fast as you can")
print("     4. Click 'enter/return' when you are done.\n")

#### Game Start Countdown
input("> Input any key to start the game! ")

print("-"*30)
print("The game will start in...")
print_slow("3...2...1!", .2)
print("-"*30,"\n")


#### 💻 YOUR CODE GOES HERE 💻 ####
# translate this pseudocode into Python code:
        # store one prompt from prompt_list in chosen_prompt
        # print chosen_prompt
        # store current time in start_time
        # store user typing input attempt in user_typed_prompt 
        # store current time in end_time 
        # store the return value of calculated_wpm() in user_wpm
        # print user_wpm
