import sys
import time
from random import choice, randint
from prompts import common_words

def print_slow(str,seconds):
    # prints one character at time with `seconds` in between

    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(seconds)
    sys.stdout.write('\n')


def calculate_wpm(user_typed_prompt, start_time, end_time):
    # returns the number of words per minute

    total_time_minutes = (end_time - start_time)/60
    user_total_keys_pressed = len(user_typed_prompt)

    total_num_words = user_total_keys_pressed/5
    wpm = total_num_words/total_time_minutes

    return round(wpm,1)


def calculate_accuracy(chosen_prompt, user_typed_prompt):
    # returns the accuracy of the user's input in a percentage

    total_characters = len(user_typed_prompt)
    correct_characters = 0
    
    for i in range(total_characters):
        if chosen_prompt[i] == user_typed_prompt[i]:
            correct_characters += 1

    accuracy = (correct_characters/total_characters)*100

    return round(accuracy,1)


def generate_prompt():
    # returns a prompt of random words of a random length 

    random_prompt = ""
    prompt_length = randint(10,15)

    for i in range(prompt_length):
        random_word = choice(common_words)
        random_prompt += random_word

        if i != prompt_length-1:
            random_prompt +=  " "

    return random_prompt