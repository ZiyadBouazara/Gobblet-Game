import json
from api import débuter_partie, récupérer_partie
from gobblet import GobbletError, interpréteur_de_commande
from joueur import Joueur, Automate
from main import SECRET
from plateau import Plateau

args = interpréteur_de_commande()
link = '/Users/ziyadbouazara/Library/Mobile Documents/com~apple~CloudDocs/GLO-1901/gobblet-phase-2-stf1/version'


class Jeu:
    def __init__(self, idul, secret, id_partie=None, automatique=False):
        if id_partie is None:
            try:
                id_partie, plateau, joueurs = débuter_partie(args.IDUL, SECRET)
                self.plateau = Plateau(plateau)

            except PermissionError:
                raise GobbletError(
                    f"L'IDUL {idul} n'est pas reconnu par le serveur.")

            except RuntimeError:
                raise GobbletError(
                    f"L'identifiant {id_partie} ne correspond pas à une partie du joueur {idul}.")

        else:
            try:
                with open(link + f"/{id_partie}.json", r) as json_file:
                    sequence_json = json.file.read()
                    _plateau = json.loads(sequence_json)
                # ? Enlever le f-string ?
                self.plateau = Plateau(_plateau.get(f'{id_partie}'))
                id_partie, plateau, joueurs = récupérer_partie(
                    id_partie, args.IDUL, SECRET)

            except PermissionError:
                raise GobbletError(
                    f"L'IDUL {idul} n'est pas reconnu par le serveur.")

            except RuntimeError:
                GobbletError(
                    f"L'identifiant {id_partie} ne correspond pas à une partie du joueur {idul}.")

        if automatique:
            self.joueur1 = Automate(joueurs[0].get(
                'nom'), 1, joueurs[0].get('piles'))
        else:
            self.joueur1 = Joueur(joueurs[0].get(
                'nom'), 1, joueurs[0].get('piles'))

        self.joueur2 = Joueur(joueurs[1].get(
            'nom'), 2, joueurs[1].get('piles'))
        self.secret = secret
        self.id_partie = id_partie
        self.automatique = automatique
        ### TO DO : IL FAUT TROUVER COMMENT ET RAJOUTER LE TRAITEMENT D'ERREUR 'GobbletError: La partie {id_partie} est terminée.'###

    def __str__(self): pass

    def jouer(self): pass
