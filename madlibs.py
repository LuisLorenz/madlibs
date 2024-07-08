
import time
import sys
import random
from word_list import all_lists

# print(all_lists['nouns_person'])
    # it works
    # when it did not work simply try to restart the terminal and try again

RED = '\033[91m'
# YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
GREEN = '\033[92m'
CYAN = '\033[96m'
RESET = '\033[0m'

# {RED}{text1}{RESET}

print("Welcome to MADLIBS!!!")


# add here the flow text function 

playstyle_test = f"""
Please select your playstyle: 

If you want to be creative and insert your own word insert '1'.
If you want the computer choose random word insert '2'.\n""" 
# check the input if it is right

for char in playstyle_test:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
    
    if char in ".!?":
        time.sleep(0.4)

    if char in ",":
        time.sleep(0.1)

playstyle = int(input('-> '))

# playstle == 1
if playstyle == 1:
    print("Please insert one word for each variable:")

    noun_1 = input("noun_1 (person) = ")
    noun_2 = input("noun_2 (person) = ")
    noun_3 = input("noun_3 (job) = ")
    noun_4 = input("noun_4 (location) = ")
    noun_5 = input("noun_5 (location) = ")

    verb_1 = input("verb_1 in infitive = ")
    verb_2 = input("verb_2 in infitive = ")
    verb_3 = input("verb_3 in simple past = ")

    adjective_1 = input("adjective_1 = ")
    adjective_2 = input("adjective_2 = ")

# playstyle == 2
elif playstyle == 2:
    noun_1 = random.choice(all_lists['nouns_person'])

    noun_2 = random.choice(all_lists['nouns_person'])
    while noun_2 == noun_1:
        noun_2 = random.choice(all_lists['nouns_person'])
        
    noun_3 = random.choice(all_lists['nouns_job'])

    noun_4 = random.choice(all_lists['nouns_location'])

    noun_5 = random.choice(all_lists['nouns_location'])
    while noun_5 == noun_4:
        noun_5 = random.choice(all_lists['nouns_location'])

    
    verb_1 = random.choice(all_lists['verbs_infinitive'])

    verb_2 = random.choice(all_lists['verbs_infinitive'])
    while verb_2 == verb_1:
        verb_2 = random.choice(all_lists['verbs_infinitive'])

    verb_3 = random.choice(all_lists['verbs_simple_past'])


    adjective_1 = random.choice(all_lists['adjectives'])

    adjective_2 = random.choice(all_lists['adjectives'])
    while adjective_2 == adjective_1:
        adjective_2 = random.choice(all_lists['adjectives'])


# else:
#     print('Your input is invalide. Please try again!')



text = f'''
In ancient {BLUE}{noun_5}{RESET}, the famous {BLUE}{noun_3} {MAGENTA}{noun_1}{RESET} was known for his {CYAN}{adjective_1}{RESET} behavior and sharp wit/charming. 

He lived in a barrel/container, owned nothing, and often roamed/strolled the streets of {BLUE}{noun_4}{RESET} with a lantern in broad daylight, claiming to be looking for an {CYAN}{adjective_2}{RESET} man. 

One day, {GREEN}{noun_2}{RESET}, having heard tales of {MAGENTA}{noun_1}{RESET} wisdom and unconventional lifestyle, decided to {RED}{verb_1}{RESET} him. 

{GREEN}{noun_2}{RESET} found {MAGENTA}{noun_1}{RESET} lounging/cilling in the sun, enjoying a simple day.

"{MAGENTA}{noun_1}{RESET}," {GREEN}{noun_2}{RESET} proclaimed, "I am {GREEN}{noun_2}{RESET} the Great, the king of all the lands you see. 

I have come to {RED}{verb_2}{RESET} the wisest man in {BLUE}{noun_5}{RESET}. 

Is there anything I can do for you?"

{MAGENTA}{noun_1}{RESET} looked up from his meal, squinted/blinked at {GREEN}{noun_2}{RESET}, and replied, "Yes, there is something you can do for me. 

Please go out of my sunlight."

Stunned, {GREEN}{noun_2}{RESET} laughed heartily. He admired/looked up to {MAGENTA}{noun_1}{RESET}' audacity and said, "If I were not {GREEN}{noun_2}{RESET}, I would wish to be {BLUE}{noun_1}{RESET}."

Without missing a beat, {MAGENTA}{noun_1}{RESET} responded, "If I were not {MAGENTA}{noun_1}{RESET}, I too would wish to be {MAGENTA}{noun_1}{RESET}."

The crowd that had gathered chuckled/gurgled at the {BLUE}{noun_3}{RESET}'s wit. 

{GREEN}{noun_2}{RESET}, amused and impressed, offered {MAGENTA}{noun_1}{RESET} a place at his court/court of law. {MAGENTA}{noun_1}{RESET} declined, saying he preferred his simple life of freedom.

As {GREEN}{noun_2}{RESET} walked away, his generals asked why he had tolerated such insolence/shamelessness. 

{GREEN}{noun_2} {RED}{verb_3}{RESET} and said, "If I were not {GREEN}{noun_2}{RESET}, I would indeed wish to be {MAGENTA}{noun_1}{RESET}."

{MAGENTA}{noun_1}{RESET} continued his days in the sun, while {GREEN}{noun_2}{RESET} went on to conquer more lands. 

Both men were legends in their own right, proving that greatness comes in many forms—whether commanding armies or simply enjoying a sunny afternoon in a barrel.
'''


for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
    
    if char in ".!?":
        time.sleep(0.5)

    if char in ",":
        time.sleep(0.2)

print()