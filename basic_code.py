# def meine_funktion():
#     print("""
#     Dies ist der erste Satz.
#     Dies ist der zweite Satz.
#     Dies ist der dritte Satz.
#     Hello
#           1
#           2
#           3
#           4
#           5
#     """)

# meine_funktion()

# #    Dies ist der erste Satz.
# #     Dies ist der zweite Satz.
# #     Dies ist der dritte Satz.
# #     Hello
# #           1
# #           2
# #           3
# #           4
# #           5


# # Definiere einige Farb-Codes
# RED = '\033[91m'
# GREEN = '\033[92m'
# YELLOW = '\033[93m'
# BLUE = '\033[94m'
# MAGENTA = '\033[95m'
# CYAN = '\033[96m'
# RESET = '\033[0m'

# # Beispiel-Variablen
# text1 = "Dies ist ein roter Text."
# text2 = "Dies ist ein grüner Text."
# text3 = "Dies ist ein gelber Text."

# # Drucke die Variablen farblich hervorgehoben
# print(f"{RED}{text1}{RESET}")
# print(f"{GREEN}{text2}{RESET}")
# print(f"{YELLOW}{text3}{RESET}")

# import time
# import sys

# # Definiere den Text, den du drucken möchtest
# text = """
#     Dies ist ein Beispieltext, der Buchstabe für Buchstabe gedruckt wird.
#     Dies ist ein Beispieltext, der Buchstabe für Buchstabe gedruckt wird.
#     Dies ist ein Beispieltext, der Buchstabe für Buchstabe gedruckt wird.
#     """

# # Schleife durch jeden Buchstaben im Text
# for char in text:
#     # Drucke den Buchstaben ohne Zeilenumbruch
#     sys.stdout.write(char)
#     sys.stdout.flush()
#     # Die Funktion sys.stdout.flush() wird verwendet, 
#     # um den Puffer des Standardausgabekanals (stdout) sofort zu leeren und den gesamten gepufferten Inhalt auf dem Bildschirm anzuzeigen. 
#     # Normalerweise wird die Ausgabe in einem Puffer gesammelt und in größeren Blöcken an den Bildschirm gesendet, 
#     # um die Effizienz zu erhöhen. Durch das Leeren des Puffers mit flush() wird sichergestellt, 
#     # dass die bis dahin gesammelten Ausgaben sofort sichtbar werden.
#     # Füge eine kleine Verzögerung hinzu
#     time.sleep(0.05)

# # Am Ende eine neue Zeile hinzufügen
# print()

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