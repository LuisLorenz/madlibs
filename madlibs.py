
import time
import sys

RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

print("Welcome to MADLIBS!!!")

print("Please insert one word for each variable:")

noun_1 = input("noun_1 = ")
noun_2 = input("noun_2 = ")
noun_3 = input("noun_3 = ")
noun_4 = input("noun_4 = ")
noun_5 = input("noun_5 = ")

verb_1 = input("verb_1 = ")
verb_2 = input("verb_2 = ")
verb_3 = input("verb_3 = ")
verb_4 = input("verb_4 = ")
verb_5 = input("verb_5 = ")

adjective_1 = input("adjective_1 = ")
adjective_2 = input("adjective_2 = ")
adjective_3 = input("adjective_3 = ")
adjective_4 = input("adjective_4 = ")
adjective_5 = input("adjective_5 = ")

text = f'''
In ancient Greece, the famous philosopher {noun_1} was known for his {adjective_5} behavior and sharp wit/charming. 

He {verb_5} in a barrel/container, owned nothing, and often roamed/strolled the streets of Athens with a lantern in broad daylight, claiming to be looking for an {adjective_1} man. 

One day, {noun_5}, having heard tales of {noun_1} wisdom and {adjective_4} lifestyle, decided to {verb_5} him. 

{noun_5} found {noun_1} lounging/cilling in the sun, enjoying a simple {noun_2}.

"{noun_1}," {noun_5} proclaimed, "I am {noun_4} the Great, the {noun_3} of all the lands you see. 

I have come to {verb_2} the wisest man in Greece. 

Is there anything I can do for you?"

{noun_1} looked up from his meal, squinted/blinked at {noun_5}, and replied, "Yes, there is something you can do for me. 

Please {verb_3} out of my {adjective_2} sunlight."

Stunned, Alexander laughed heartily. He admired/looked up to Diogenes' audacity and said, "If I were not Alexander, I would wish to be Diogenes."

Without missing a beat, Diogenes responded, "If I were not Diogenes, I too would wish to be Diogenes."

The crowd that had gathered chuckled/gurgled at the philosopher's wit. 

Alexander, amused and impressed, offered Diogenes a place at his court/court of law. Diogenes declined, saying he preferred his simple life of freedom.

As Alexander walked away, his generals asked why he had tolerated such insolence/shamelessness. 

Alexander smiled and said, "If I were not Alexander, I would indeed wish to be Diogenes."

Diogenes continued his days in the sun, while Alexander went on to conquer more lands. 

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