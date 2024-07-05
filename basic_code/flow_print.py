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
    # Die Funktion sys.stdout.flush() wird verwendet, 
    # um den Puffer des Standardausgabekanals (stdout) sofort zu leeren und den gesamten gepufferten Inhalt auf dem Bildschirm anzuzeigen. 
    # Normalerweise wird die Ausgabe in einem Puffer gesammelt und in größeren Blöcken an den Bildschirm gesendet, 
    # um die Effizienz zu erhöhen. Durch das Leeren des Puffers mit flush() wird sichergestellt, 
    # dass die bis dahin gesammelten Ausgaben sofort sichtbar werden.
    # Füge eine kleine Verzögerung hinzu
    time.sleep(0.05)

# Am Ende eine neue Zeile hinzufügen
print()