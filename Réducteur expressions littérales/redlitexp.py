#! /usr/bin/env python3

# Fait avec l'aide de ChatGPT

import sympy as sp

def develop_and_reduce(expression_str):
    """
    Développe et réduit une expression littérale.
    
    Args:
        expression_str (str): L'expression mathématique en chaîne de caractères.
    
    Returns:
        tuple: L'expression développée et l'expression réduite.
    """
    # Convertir l'expression en une forme manipulable
    expression = sp.sympify(expression_str)
    
    # Développer l'expression
    developed = sp.expand(expression)
    
    # Réduire l'expression
    reduced = sp.simplify(expression)
    
    return developed, reduced

if __name__ == "__main__":
    # Entrée de l'utilisateur
    expression_input = input("Entrez une expression littérale (ex: (x + 1)**2 - x*(x + 2)): ")

    try:
        # Calculer le développement et la réduction
        developed, reduced = develop_and_reduce(expression_input)
        
        # Afficher les résultats
        print(f"\nExpression développée : {developed}")
        print(f"Expression réduite : {reduced}")
    except Exception as e:
        print(f"Erreur lors de l'analyse de l'expression : {e}")
