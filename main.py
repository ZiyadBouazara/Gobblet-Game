from pathlib import Path

from api import lister_parties
from gobblet import formater_les_parties, interpréteur_de_commande
from jeu import Jeu

SECRET = "ed0f6548-6830-4e2a-9ffb-4c6d94e5b28b"


def demander_partie_a_continuer(parties):
    if not parties:
        # Il n'y a pas de parties à continuer
        return None
    while True:
        print(formater_les_parties(parties))
        choix = input("Entrez le numéro de la partie à continuer: ")
        if not choix.isdigit():
            print(f"Vous devez entrer un nombre.")
            continue
        choix = int(choix)
        if not (1 <= choix <= len(parties)):
            print(f"Vous devez entrer un nombre de 1 à {len(parties)}.")
            continue
        return parties[choix - 1]["id"]


def lister_les_parties(idul, secret):
    chemin_de_sauvegarde = Path(__file__).parent / "sauvegarde"
    identifiants = []
    parties = []
    if not chemin_de_sauvegarde.exists():
        # le dossier n'existe pas
        return parties

    for file in chemin_de_sauvegarde.iterdir():
        identifiants.append(file.stem)

    # On récupère les 20 dernières parties du serveur
    for partie in lister_parties(idul, secret):
        if partie["id"] not in identifiants:
            # Il ne s'agit pas d'une partie sauvegardée localement
            # Ça pourrait être une veille partie de la phase 1 ou 2
            # Où une partie appartenant à un joueur différent
            # On continue avec l'élément suivant
            continue
        parties.append(partie)

    return parties


if __name__ == "__main__":
    args = interpréteur_de_commande()
    id_partie = None

    if args.lister:
        parties = lister_les_parties(args.IDUL, SECRET)
        id_partie = demander_partie_a_continuer(parties)

    jeu = Jeu(args.IDUL, SECRET, id_partie=id_partie,
              automatique=args.automatique)
    jeu.jouer()
