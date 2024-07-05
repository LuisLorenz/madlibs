
## update: flowing print + pause at every end of sentence
import time
import sys

# Definiere den Text, den du drucken möchtest
text = """
Dies ist ein Beispieltext, der Buchstabe für Buchstabe gedruckt wird.
Dies ist ein Beispieltext, der Buchstabe für Buchstabe gedruckt wird.
Dies ist ein Beispieltext, der Buchstabe für Buchstabe gedruckt wird.
"""

# Schleife durch jeden Buchstaben im Text
for char in text:
    # Drucke den Buchstaben ohne Zeilenumbruch
    sys.stdout.write(char)
    sys.stdout.flush()
    # Füge eine kleine Verzögerung hinzu
    time.sleep(0.05)
    
    # Überprüfen, ob das aktuelle Zeichen ein Satzendezeichen ist
    if char in ".!?":
        # Eine zusätzliche Verzögerung nach Satzende einfügen
        time.sleep(0.5)

# Am Ende eine neue Zeile hinzufügen
print()

# plain code
import time
import sys


text = """
x
x
x
"""

for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
    
    if char in ".!?":
        time.sleep(0.5)

print()