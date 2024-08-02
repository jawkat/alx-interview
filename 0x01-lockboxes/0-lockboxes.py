#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys
"""

def canUnlockAll(boxes):
    """
    Détermine si toutes les boîtes peuvent être ouvertes.

    :param boxes: Liste de listes, où chaque sous-liste contient des clés.
    :return: True si toutes les boîtes peuvent être ouvertes, sinon False.
    """
    n = len(boxes)  # Nombre total de boîtes
    opened = [False] * n  # Liste pour suivre les boîtes ouvertes
    opened[0] = True  # La boîte 0 est ouverte

    to_explore = [0]  # Commencer avec la boîte 0

    while to_explore:
        current_box = to_explore.pop()  # Prendre une boîte de la pile
        for key in boxes[current_box]:
            if key < n and not opened[key]:
                opened[key] = True  # Marquer la boîte comme ouverte
                to_explore.append(key)  # Ajouter cette boîte à la pile

    for status in opened:
        if not status:
            return False  # Si une boîte n'est pas ouverte, retourner False
    return True  # Si toutes les boîtes sont ouvertes, retourner True
