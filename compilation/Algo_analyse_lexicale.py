def carsuiv(chaine, index):
    if index < len(chaine):
        return chaine[index], index + 1
    else:
        return None, index  # End of file (EOF)

def transister(etat, position, tableTransition):
    return tableTransition[etat][position]

def analayseurLexical(chaine,symboles,tableTransition,etatsFinaux,etatInitial):
    index = 0
    e = etatInitial
    while True:
        ch, index = carsuiv(chaine, index)
        if ch is None:
            break
        position = symboles.index(ch)   
        e = transister(e, position, tableTransition)
        print(f'etat actuel: {e}, symbole lu: {ch}')
    if e in etatsFinaux:
        return True
    else:
        return False