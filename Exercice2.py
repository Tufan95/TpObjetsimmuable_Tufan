from dataclasses import dataclass, replace
import asyncio
import random

# --- Question 1 : Structure de données immuable ---
@dataclass(frozen=True)
class Personne:
    nom: str
    age: int

# --- Question 2 : Fonction anniversaire ---
def anniversaire(personnes):
    """ Retourne une nouvelle liste avec l'âge de chaque personne augmenté de 1 """
    return [replace(p, age=p.age + 1) for p in personnes]

# --- Question 3 : Promesse getRandomNumber ---
async def getRandomNumber():
    """ Simule une promesse retournant un nombre aléatoire après 1 seconde """
    await asyncio.sleep(1)
    return random.randint(1, 100)

# --- Question 4 : Générer et afficher deux nombres ---
async def test_multiple():
    numbers = await asyncio.gather(getRandomNumber(), getRandomNumber())
    print("Deux nombres générés :", numbers)

# --- TESTS ---
# Création d'une liste de personnes
personnes = [Personne("Alice", 29), Personne("Bob", 28)]
print("Liste avant anniversaire :", personnes)
print("Liste après anniversaire :", anniversaire(personnes))

# Exécution de la génération asynchrone
asyncio.run(test_multiple())
