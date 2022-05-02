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
        while True:
            print(self.__str__(self.plateau, [self.joueur1, self.joueur2]))
            origine, destination = self.joueur1.récupérer_le_coup(self.plateau)

            if origine == 'stop' or destination == 'stop':
                dictionnaire = {self.id_partie: self.plateau.état_plateau()}
                with open(link + f"/{self.id_partie}.json", 'w') as json_file:
                    json.dump(dictionnaire, json_file)
                break

            if len(str(origine)) == 1:
                g1 = self.joueur1.retirer_gobblet(origine)

            else:
                g1 = self.plateau.retirer_gobblet(origine[0], origine[1])

            self.plateau.placer_gobblet(destination[0], destination[1], g1)

            print(origine, len(destination))

            id_partie, plateau, joueurs = jouer_coup(
                self.id_partie, origine, destination, args.IDUL, SECRET)

            self.id_partie = id_partie

            for number, (initial, final) in enumerate(zip(self.joueur2.piles, joueurs[1]['piles'])):

                if not isinstance(initial, Gobblet):
                    continue

                if initial.grosseur != final[1]:
                    g2 = self.joueur2.retirer_gobblet(number)

                if initial.grosseur == 0 and len(final) == 0:
                    g2 = self.joueur2.retirer_gobblet(number)
                    break

            for index1, (x, y) in enumerate(zip(self.plateau.plateau, plateau)):
                for index2, (a, b) in enumerate(zip(x, y)):

                    if len(a) != 0 and len(b) != 0:
                        if a[-1].grosseur != b[1]:
                            self.plateau.placer_gobblet(index2, 3-index1, g2)

                    if len(a) == 0 and len(b) == 0:
                        continue

                    if len(a) == 0 and len(b) != 0:
                        self.plateau.placer_gobblet(index2, 3-index1, g2)
