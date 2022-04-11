"""Module Gobblet

Attributes:
    GOBBLET_REPRÉSENTATION (dict): Constante représentant les gobelets des joueurs.

Functions:
    * Gobblet - Classe représentant un Gobblet.
    * GobbletError - Classe gérant les exceptions GobbletError.
    * interpréteur_de_commande - Génère un interpréteur de commande.
    * formater_jeu - Formater la représentation graphique d'un jeu.
    * formater_les_parties - Formater la liste des dernières parties.
"""

from argparse import ArgumentParser

# Voici la représentation des Gobblets, n'hésitez pas à l'utiliser.
# 1 pour le joueur 1, 2 pour le joueur 2.
GOBBLET_REPRÉSENTATION = {
    1: ["▫", "◇", "◯", "□"],
    2: ["▪", "◆", "●", "■"],
}


class GobbletError(Exception):
    def __str__(self):
        return f"GobbletError: {self.args[0]}"


class Gobblet:
    """
    Gobblet
    """

    def __init__(self, grosseur, no_joueur):
        """Constructeur de gobelet.

        Ne PAS modifier cette méthode.

        Args:
            grosseur (int): Grosseur du Gobblet [0, 1, 2, 3].
            no_joueur (int): Numéro du joueur [1, 2].
        """
        self.grosseur, self.no_joueur = self.valider_gobblet(
            grosseur, no_joueur)

    def valider_gobblet(self, grosseur, no_joueur):
        """Validateur de gobelet.

        Args:
            grosseur (int): la grosseur du gobelet [0, 1, 2, 3].
            no_joueur (int): le numéro du joueur [1, 2].

        Returns:
            tuple[int, int]: un tuple contenant la grosseur et le numéro du joueur.

        Raises:
            GobbletError: La grosseur doit être un entier.
            GobbletError: La grosseur doit être comprise entre 0 et 3.
            GobbletError: Le numéro du joueur doit être un entier.
            GobbletError: Le numéro du joueur doit être 1 ou 2.
        """
        if isinstance(grosseur, int) == False:
            raise GobbletError('La grosseur doit être un entier')
        if grosseur not in [0, 1, 2, 3]:
            raise GobbletError('La grosseur doit être comprise entre 0 et 3')
        if isinstance(no_joueur, int) == False:
            raise GobbletError('Le numéro du joueur doit être un entier')
        if no_joueur not in [1, 2]:
            raise GobbletError('Le numéro du joueur doit être 1 ou 2')
        return (grosseur, no_joueur)

    def __str__(self):
        """Formater un gobelet.

        Returns:
            str: Représentation du gobelet pour le joueur.
        """
        if self == []:
            affichage = '   '
        else:
            affichage = ' ' + \
                GOBBLET_REPRÉSENTATION[self.no_joueur][self.grosseur] + ' '
        return affichage

    def __eq__(self, autre):
        """Comparer l'équivalence de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si les deux gobelets sont de même taille.
        """
        return isinstance(autre, Gobblet) and isinstance(self, Gobblet) and (self.grosseur == autre.grosseur)

    def __gt__(self, autre):
        """Comparer la grosseur de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet est plus gros que l'autre.
        """
        if self.no_joueur == 1:
            return isinstance(autre, Gobblet) and isinstance(self, Gobblet)\
                and (self.grosseur < autre.grosseur)
        else:
            return isinstance(autre, Gobblet) and isinstance(self, Gobblet)\
                and (autre.grosseur < self.grosseur)

    def __lt__(self, autre):
        """Comparer la grosseur de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet est plus petit que l'autre.
        """
        return not (Gobblet.__eq__(self, autre) or Gobblet.__gt__(self, autre))

    def __ne__(self, autre):
        """Comparer l'équivalence de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet n'est pas équivalent à l'autre.
        """
        return not Gobblet.__eq__(self, autre)

    def __ge__(self, autre):
        """Comparer la grosseur de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet est plus grand ou égal à l'autre.
        """
        return not Gobblet.__gt__(self, autre)

    def __le__(self, autre):
        """Comparer la grosseur de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet est plus petit ou égal à l'autre.
        """
        return Gobblet.__eq__(self, autre) or Gobblet.__gt__(self, autre)

    def état_gobblet(self):
        """Obtenir l'état du gobelet.

        Returns:
            list: la paire d'entiers représentant l'état du gobelet (numéro du joueur et grosseur du gobelet).
        """
        return [self.no_joueur, self.grosseur]


def interpréteur_de_commande():
    """Interpreteur de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par parser.parse_args().
        Cette objet aura l'attribut IDUL représentant l'idul du joueur
        et l'attribut lister qui est un booléen True/False.
    """
    parser = ArgumentParser(description='Gobblet')
    parser.add_argument('IDUL', help='IDUL du joueur')
    parser.add_argument('-l', '--lister',
                        action='store_true', help='Lister les parties existantes')
    return parser.parse_args()


def formater_jeu(plateau, joueurs):
    """Formater un jeu.

    Args:
        plateau (Plateau): le plateau de jeu.
        joueurs (list): la liste des deux Joueurs.

    Returns:
        str: Représentation du jeu.
    """
    r = ''
    len1 = len(joueurs[0].nom)
    len2 = len(joueurs[1].nom)
    espace = max(len1, len2) - min(len1, len2)
    for i, e in enumerate(joueurs):
        if i == 0 and len1 < len2:
            r += ' '*espace + e.__str__() + '\n'
        elif i == 1 and len2 < len1:
            r += ' '*espace + e.__str__() + '\n'
        else:
            r += e.__str__() + '\n'
    return " "*(max(len1, len2) + 3) + "0   1   2 \n" + r + '\n' + plateau.__str__()


def formater_les_parties(parties):
    """Formater une liste de parties.

    L'ordre doit être exactement la même que ce qui est passé en paramètre.

    Args:
        parties (list): une liste des parties.

    Returns:
        str: Représentation des parties.
    """
    représentation = ''
    for y, i in enumerate(parties):
        représentation += f'{y} : {i["date"]}, {i["joueurs"][0]} vs {i["joueurs"][1]}'
        if i["gagnant"] is not None:
            représentation += f', gagnant: {i["gagnant"]}\n'
        else:
            représentation += '\n'
    return représentation
