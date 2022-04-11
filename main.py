# -*- coding: utf-8 -*-
"""Jeu Gobblet

Ce programme permet de joueur au jeu Gobblet.
"""
from api import débuter_partie, lister_parties, jouer_coup
from gobblet import (
    formater_jeu,
    formater_les_parties,
    interpréteur_de_commande,
)
from joueur import Joueur
from plateau import Plateau

# Mettre ici votre secret récupérer depuis le site de PAX
SECRET = "ed0f6548-6830-4e2a-9ffb-4c6d94e5b28b"


if __name__ == "__main__":
    args = interpréteur_de_commande()
    if args.lister:
        parties = lister_parties(args.IDUL, SECRET)
        print(formater_les_parties(parties))
    else:
        id_partie, plateau, joueurs = débuter_partie(args.IDUL, SECRET)
        while True:
            # Implémentez votre boucle de jeu
            joueur1 = Joueur(joueurs[0].get('nom'), 1, joueurs[0].get('piles'))
            joueur2 = Joueur(joueurs[1].get('nom'), 2, joueurs[1].get('piles'))
            plateau_de_jeux = Plateau(plateau)
            print(formater_jeu(plateau_de_jeux, [joueur1, joueur2]))
            origine, destination = joueur1.récupérer_le_coup(plateau_de_jeux)
            id_partie, plateau, joueurs = jouer_coup(
                id_partie, origine, destination, args.IDUL, SECRET)
