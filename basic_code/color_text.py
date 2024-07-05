# Definiere einige Farb-Codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

# Beispiel-Variablen
text1 = "Dies ist ein roter Text."
text2 = "Dies ist ein grüner Text."
text3 = "Dies ist ein gelber Text."

# Drucke die Variablen farblich hervorgehoben
print(f"{RED}{text1}{RESET}")
print(f"{GREEN}{text2}{RESET}")
print(f"{YELLOW}{text3}{RESET}")