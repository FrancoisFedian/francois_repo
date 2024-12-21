#!/usr/bin/env python3

# Généré par ChatGPT

import time

def pseudo_random(seed=None, iterations=10, digits=None, min_val=None, max_val=None):
    # Si pas de seed, on utilise le timestamp actuel
    if seed is None:
        seed = int(time.time() * 1000)  # Timestamp en millisecondes

    result = seed
    for _ in range(iterations):
        # Convertir le nombre en chaîne de caractères
        str_result = str(result)
        # On prend les 4 chiffres du milieu
        start = max(0, len(str_result)//2 - 2)
        end = min(len(str_result), len(str_result)//2 + 2)
        middle = str_result[start:end]
        
        # Si la chaîne est plus petite que 4 chiffres, on rajoute des zéros
        middle = middle.ljust(4, '0')
        # Calculer le carré de ce nombre
        result = int(middle) ** 2

        # Limiter à une taille de chiffres si spécifié
        if digits is not None:
            result = int(str(result)[:digits])  # Garde seulement le nombre de chiffres demandé

        # Limiter à la plage min/max si spécifié
        if min_val is not None and max_val is not None:
            result = min(max(result, min_val), max_val)

    return result


# Demander à l'utilisateur de choisir une option
def get_user_input():
    choice = input("Voulez-vous un nombre aléatoire avec un certain nombre de chiffres (1) ou dans une plage (2) ? (1/2): ")

    if choice == '1':
        digits = int(input("Combien de chiffres voulez-vous ? "))
        return pseudo_random(digits=digits)

    elif choice == '2':
        min_val = int(input("Entrez la valeur minimale: "))
        max_val = int(input("Entrez la valeur maximale: "))
        return pseudo_random(min_val=min_val, max_val=max_val)

    else:
        print("Choix invalide. Essayez à nouveau.")
        return get_user_input()

# Exemple d'utilisation
random_number = get_user_input()
print(f"Le nombre généré est : {random_number}")
