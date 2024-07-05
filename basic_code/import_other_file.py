# quick and dirty
# slower! and less readable

# # listen.py
# meine_liste_1 = [1, 2, 3]
# meine_liste_2 = [4, 5, 6]
# meine_liste_3 = [7, 8, 9]   

###################################################
# # main.py
# from listen import *

# # Jetzt können Sie alle Listen verwenden
# print(meine_liste_1)
# print(meine_liste_2)
# print(meine_liste_3)

# solution with dictionary
# listen.py
meine_liste_1 = [1, 2, 3]
meine_liste_2 = [4, 5, 6]
meine_liste_3 = [7, 8, 9]

# Ein Dictionary, das alle Listen enthält
alle_listen = {
    'meine_liste_1': meine_liste_1,
    'meine_liste_2': meine_liste_2,
    'meine_liste_3': meine_liste_3,
}
###################################################
# main.py
from listen import alle_listen

# Jetzt können Sie alle Listen verwenden
print(alle_listen['meine_liste_1'])
print(alle_listen['meine_liste_2'])
print(alle_listen['meine_liste_3'])