from AutomateFiniDeterministe import Automate
from Algo_analyse_lexicale import analayseurLexical

A = Automate()

a = int(input('nombre d etats'))
A.setEtats(a)

a = int(input('etat initial'))
A.setEtatInitial(a)

a = int(input('nombre d etats finaux'))
A.setEtatsFinaux(a)

a = int(input('nombre de symboles'))
A.setSymboles(a)

A.setTableTransition()

print(f'ETATS: {A.getEtats()}')
print(f'ETAT INITIAL : {A.getEtatInitial()}')
print(f'ETATS FINAUX: {A.getEtatsFinaux()}')
print(f'SYMBOLES: {A.getSymboles()}')
A.getTableTransition()


etats = A.getEtats()
etatInitial = A.getEtatInitial()
etatsFinaux = A.getEtatsFinaux()
symboles = A.getSymboles()
tableTransition = A.getTableTransition()
boucle = True
while boucle:
    while True:   # saisie d'une chaine correcte
        chaine = input('entrez la chaine a analyser: ')
        validite = True
        for ch in chaine:
            if ch not in symboles:
                print(f'le caractere {ch} n est pas contenu dans la table des symboles')
                validite = False
                break  # Exit the for loop if an invalid character is found
        if validite:
            break  # Exit the while loop if the chaine is valid
    
    if analayseurLexical(chaine,symboles,tableTransition,etatsFinaux,etatInitial):
        print(f"la chaine {chaine} est acceptee")
    else:
        print(f"la chaine {chaine} est rejetee")

    R = input("\nanalyse terminee voulez vous repeter 'oui' ou 'non' ")
    if R == 'non':
        boucle = False