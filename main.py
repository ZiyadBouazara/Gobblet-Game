# -*- coding: utf-8 -*-
"""Jeu Gobblet

Ce programme permet de joueur au jeu Gobblet.
"""
from api import débuter_partie, lister_parties, jouer_coup, récupérer_partie
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
        #Étapes à suivre pour lister et poursuivre:
        #1 utiliser la fonction input afin de demander à l'utilisateur le numéro de la partie qu'il choisit de continuer dans la liste de parties qu'on lui a print
 
        #2 si la valeur, le numéro de la partie dans la liste de parties n'est pas valide, reposer la question jusqu'à ce qu'elle le soit

        nombre_de_parties = len(parties)
        while True:
            try:
                partie_choisie = int(input("Choisissez le numéro de partie: "))
            except ValueError:
                print("Désolé, le numéro de partie doit être un nombre entier")
                #Try again, return to the start of the loop
                continue
            if partie_choisie < 0 or partie_choisie > len(parties):
                print("Désolé, le numéro de partie doit être compris dans les parties existantes")
                #Try again, return to the start of the loop
                continue
            else:
                #la valeur est valide, on peut exit le loop
                break

        #3 une fois la partie sélectionnée la boucle de jeu doit afficher l'état de la partie afin de la poursuivre selon le mode choisi
        partie_récupérée = récupérer_partie(str(partie_choisie), args.IDUL, SECRET)
        print(partie_récupérée)


        # Si dans le command line on a spécifié vouloir continuer en automatique voici la boucle de jeu spécial:
        if args.automatique:
            #Implémenter la boucle de jeu en automatique
            a = "a" #j'ai mis 'a' seulement pour pas que vscode mettent un problème ici en attendant qu'on implémente la boucle
        
        # Sinon on continu par défaut, soit en manuel
        else: 
            id_partie, plateau, joueurs = partie_récupérée
            #On conserve la même boucle de jeu que lorsqu'on command line 'python main.py IDUL', sauf qu'on commence avec 
            #récupérer partie plutôt que débuter partie?
            # si oui:
            while True:
                # Implémentez votre boucle de jeu
                joueur1 = Joueur(joueurs[0].get('nom'), 1, joueurs[0].get('piles'))
                joueur2 = Joueur(joueurs[1].get('nom'), 2, joueurs[1].get('piles'))
                plateau_de_jeux = Plateau(plateau)
                print(formater_jeu(plateau_de_jeux, [joueur1, joueur2]))
                origine, destination = joueur1.récupérer_le_coup(plateau_de_jeux)
                id_partie, plateau, joueurs = jouer_coup(
                    id_partie, origine, destination, args.IDUL, SECRET)


    elif args.automatique is True and args.lister is False:
        # Implémentez la boucle de jeu en automatique
        a = 'a' #j'ai mis 'a' seulement pour pas que vscode mettent un problème ici en attendant qu'on implémente la boucle

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


#print(interpréteur_de_commande())
