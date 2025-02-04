def addToEach(n, lst):
    """ Ajoute n à chaque élément de la liste sans modifier la liste originale """
    return list(map(lambda x: x + n, lst))

def removeDuplicates(lst):
    """ Retourne une nouvelle liste sans doublons, sans modifier la liste originale """
    return list(set(lst))

# --- TEST ---
numbers = [1, 2, 3, 3, 4, 4, 5]
print("Liste après ajout de 3 :", addToEach(5, numbers))  # [4, 5, 5, 6, 7, 7, 8]
print("Liste sans doublons :", removeDuplicates(numbers))  # [1, 2, 3, 4, 5]
