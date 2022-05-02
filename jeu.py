import json
from api import débuter_partie, récupérer_partie, jouer_coup
from gobblet import Gobblet, GobbletError, interpréteur_de_commande
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
                with open(link + f"/{id_partie}.json", 'r') as json_file:
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

    def __str__(self, plateau, joueurs):
        indice0 = len(joueurs[0].nom)
        indice1 = len(joueurs[1].nom)
        indice_max = max([indice0, indice1])

        sortie = (f"{indice_max*' '}  0  1  2 \n"
                  f"{(indice_max - indice0) * ' '}{joueurs[0]}\n"
                  f"{(indice_max - indice1) * ' '}{joueurs[1]}\n\n{plateau}"
                  )
        return sortie

    def jouer(self):
        while True:
            print(self.__str_(self.plateau, [self.joueur1, self.joueur2]))
            origine, destination = self.joueur1.récupérer_le_coup(self.plateau)

            if origine == 'stop' or destination == 'stop':
                dico = {self.id_partie: self.plateau.état_plateau()}
                with open(link + f"/{self.id_partie}.json", 'w') as json_file:
                    json.dump(dico, json_file)
                break
            if len(str(origine)) == 1:
                gob = self.joueur1.retirer_gobblet(origine)
            else:
                gob = self.plateau.retirer_gobblet(origine[0], origine[1])
            self.plateau.placer_gobblet(destination[0], destination[1], gob)

            print(origine, len(destination))

            id_partie, plateau, joueurs = jouer_coup(
                self.id_partie, origine, destination, args.IDUL, SECRET)
            self.id_partie = id_partie

            for no_pile, (old_pile, new_pile) in enumerate(zip(self.joueur2.piles, joueurs[1].get('piles'))):
                if not isinstance(old_pile, Gobblet):
                    continue
                if old_pile.grosseur == 0 and len(new_pile) == 0:
                    gob2 = self.joueur2.retirer_gobblet(no_pile)
                    break
                if old_pile.grosseur != new_pile[1]:
                    gob2 = self.joueur2.retirer_gobblet(no_pile)

            for i, (old_line, new_line) in enumerate(zip(self.plateau.plateau, plateau)):
                for j, (old_case, new_case) in enumerate(zip(old_line, new_line)):
                    if len(old_case) == 0 and len(new_case) == 0:
                        continue
                    if len(old_case) == 0 and len(new_case) != 0:
                        self.plateau.placer_gobblet(j, 3-i, gob2)
                    if len(old_case) != 0 and len(new_case) != 0:
                        if old_case[-1].grosseur != new_case[1]:
                            self.plateau.placer_gobblet(j, 3-i, gob2)
