from dataclasses import dataclass, replace
from typing import List
import asyncio
import random

# --- Question 1 : Détection des stocks faibles et réapprovisionnement automatique ---
@dataclass(frozen=True)
class Article:
    nom: str
    prix: float
    quantite: int

def detecter_stock_faible(inventaire, seuil=3):
    """ Détecte les articles dont le stock est inférieur au seuil """
    return [article for article in inventaire if article.quantite < seuil]

def reapprovisionner_stock(inventaire, articles_a_reappro, quantite_reappro=10):
    """ Passe une commande de réapprovisionnement pour les articles en manque de stock """
    return [replace(article, quantite=article.quantite + quantite_reappro) if article in articles_a_reappro else article for article in inventaire]

# --- Question 2 : Intégration des fournisseurs externes ---
@dataclass(frozen=True)
class Fournisseur:
    nom: str
    url_api: str

def commander_chez_fournisseur(fournisseur, article, quantite):
    """ Simule une requête API pour commander un article chez un fournisseur """
    print(f"Commande passée chez {fournisseur.nom} : {quantite}x {article.nom}")
    return replace(article, quantite=article.quantite + quantite)

# --- Question 3 : Traitement asynchrone des commandes ---
@dataclass(frozen=True)
class Commande:
    articles: List[Article]

async def traiter_commande_async(commande):
    """ Simule un traitement asynchrone d'une commande avec un délai """
    await asyncio.sleep(random.uniform(1, 3))  # Simule un temps de traitement aléatoire
    print(f"Commande traitée : {commande}")

async def traiter_plusieurs_commandes(commandes):
    """ Exécute plusieurs traitements en parallèle """
    await asyncio.gather(*(traiter_commande_async(cmd) for cmd in commandes))

# --- Question 4 : Mesures de sécurité pour les données sensibles ---
def mesures_de_securite():
    """ Liste des mesures de sécurité pour protéger les données sensibles """
    print("\n🔒 Mesures de Sécurité :")
    print("- Stockage sécurisé avec base de données cryptée (ex: PostgreSQL avec pgcrypto).")
    print("- Sécurisation des transactions avec chiffrement AES.")
    print("- Authentification des utilisateurs avec tokens JWT.")
    print("- Protection contre les injections SQL et attaques XSS.")
    print("- Surveillance des accès et journaux d’audit pour prévenir les fraudes.")

# --- Question 5 : Application des principes fonctionnels ailleurs ---
def applications_programmation_fonctionnelle():
    """ Exemples d'utilisation des principes fonctionnels dans d'autres domaines """
    print("\n🚀 Applications de la programmation fonctionnelle :")
    print("1️⃣ Développement Web : React.js (Redux), GraphQL.")
    print("2️⃣ Intelligence Artificielle : Manipulation efficace des données (TensorFlow).")
    print("3️⃣ Blockchain : Transactions immuables, Smart Contracts en Solidity.")

# --- TESTS ---
# Création d'un inventaire initial
inventaire = [
    Article("Chaise", 50, 2),  # Stock faible
    Article("Table", 150, 5),  # Stock suffisant
    Article("Lampe", 30, 1)   # Stock faible
]

# Détection des stocks faibles
articles_faibles = detecter_stock_faible(inventaire)
print("🛑 Articles avec stock faible :", articles_faibles)

# Réapprovisionnement des stocks
inventaire = reapprovisionner_stock(inventaire, articles_faibles)
print("✅ Inventaire après réapprovisionnement :", inventaire)

# Intégration des fournisseurs externes
fournisseur1 = Fournisseur("FournisseurA", "https://api.fournisseura.com")
article_manquant = Article("Bureau", 200, 0)

article_reappro = commander_chez_fournisseur(fournisseur1, article_manquant, 5)
print("✅ Article après réapprovisionnement :", article_reappro)

# Traitement asynchrone des commandes
commandes = [
    Commande([Article("Chaise", 50, 1)]),
    Commande([Article("Table", 150, 1)]),
    Commande([Article("Lampe", 30, 2)])
]

print("\n⏳ Traitement des commandes en parallèle...")
asyncio.run(traiter_plusieurs_commandes(commandes))

# Mesures de sécurité
mesures_de_securite()

# Applications des principes fonctionnels
applications_programmation_fonctionnelle()
