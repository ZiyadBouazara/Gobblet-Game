import json
from api import débuter_partie, récupérer_partie, jouer_coup
from gobblet import Gobblet, GobbletError, interpréteur_de_commande
from joueur import Joueur, Automate
from plateau import Plateau

args = interpréteur_de_commande()
link = '/Users/ziyadbouazara/Library/Mobile Documents/com~apple~CloudDocs/GLO-1901/gobblet-phase-2-stf1/version'
SECRET = "ed0f6548-6830-4e2a-9ffb-4c6d94e5b28b"


class Jeu:
    def __init__(self, idul, secret, id_partie=None, automatique=False):
        if id_partie is not None:
            try:
                with open(link + f"/{id_partie}.json", 'r') as json_file:
                    sequence_json = json.file.read()
                    _plateau = json.loads(sequence_json)
                # ? Enlever le f-string ?
                self.plateau = Plateau(_plateau[f'{id_partie}'])
                id_partie, plateau, joueurs = récupérer_partie(
                    id_partie, args.IDUL, SECRET)

            except PermissionError:
                raise GobbletError(
                    f"L'IDUL {idul} n'est pas reconnu par le serveur.")

            except RuntimeError:
                GobbletError(
                    f"L'identifiant {id_partie} ne correspond pas à une partie du joueur {idul}.")

        else:
            try:
                id_partie, plateau, joueurs = débuter_partie(args.IDUL, SECRET)
                self.plateau = Plateau(plateau)

            except RuntimeError:
                raise GobbletError(
                    f"L'identifiant {id_partie} ne correspond pas à une partie du joueur {idul}.")

            except PermissionError:
                raise GobbletError(
                    f"L'IDUL {idul} n'est pas reconnu par le serveur.")

        if automatique:
            self.joueur1 = Automate(joueurs[0]['nom'], 1, joueurs[0]['piles'])
        else:
            self.joueur1 = Joueur(joueurs[0]['nom'], 1, joueurs[0]['piles'])

        self.joueur2 = Joueur(joueurs[1]['nom'], 2, joueurs[1]['piles'])
        self.secret = secret
        self.id_partie = id_partie
        self.automatique = automatique
        ### TO DO : IL FAUT TROUVER COMMENT ET RAJOUTER LE TRAITEMENT D'ERREUR 'GobbletError: La partie {id_partie} est terminée.'###

    def __str__(self, plateau, joueurs):
        x = len(joueurs[0].nom)
        y = len(joueurs[1].nom)
        z = max(x, y)
        result_out = (" "*(max(x, y) + 3) + "0   1   2 \n"
                      f"{(z - x) * ' '}{joueurs[0]}\n"
                      f"{(z - y) * ' '}{joueurs[1]}\n\n{plateau}"
                      )
        return result_out

    def jouer(self):
        pass
