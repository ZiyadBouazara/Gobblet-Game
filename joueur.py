"""Module Joueur

Functions:
    * Joueur - Classe représentant un joueur de Gobblet.
"""

from gobblet import Gobblet, GobbletError
from plateau import Plateau


class Joueur:
    """
    Joueur de Gobblet.
    """

    def __init__(self, nom, no_joueur, gobelets):
        """Constructeur de joueur.

        Ne PAS modifier cette méthode.

        Args:
            nom (str): le nom du joueur.
            no_joueur (int): le numéro du joueur (1 ou 2).
            gobelets (list): une liste des trois gobelets disponibles pour ce joueur,
            par exemple [[1, 1], [], [1, 2]], où la paire [1, 2]
            représente le numéro du joueur (1) et la grosseur du gobelet (2).
        """
        self.nom, self.no_joueur, self.piles = self.valider_joueur(
            nom, no_joueur, gobelets)

    def valider_joueur(self, nom, no_joueur, gobelets):
        """Validateur de Joueur.

        Args:
            nom (str): le nom du joueur.
            no_joueur (int): le numéro du joueur (1 ou 2).
            gobelets (list): une liste des trois gobelets disponibles pour ce joueur,
                             par exemple [[1, 1], [], [1, 2]], où la paire [1, 2]
                             représente le numéro du joueur (1) et la grosseur du gobelet (2).

        Returns:
            tuple[str, int, list]: Un tuple contenant
                                    - le nom du joueur;
                                    - son numéro;
                                    - une liste d'objets Gobblet (None pour une pile vide).

        Raises:
            GobbletError: Le nom du joueur doit être une chaine de caractères non vide.
            GobbletError: Le numéro du joueur doit être 1 ou 2.
            GobbletError: Les piles de gobelets doivent être spécifiés sous la forme d'une liste.
            GobbletError: Le joueur doit possèder 3 piles.
            GobbletError: Une pile doit être une liste de deux entiers ou une liste vide.
        """
        if len(nom) <= 0:  # Les Raises d'erreurs
            raise GobbletError(
                "Le nom du joueur doit être une chaine de caractères non vide")
        if no_joueur not in [1, 2]:
            raise GobbletError("Le numéro du joueur doit être 1 ou 2")
        for pile in gobelets:
            if isinstance(pile, list) is False:
                raise GobbletError(
                    "Les piles de gobelets doivent être spécifiés sous la forme d'une liste")
            for i in pile:  # 5ieme Erreur
                if isinstance(i, int) is False or len(pile) != 2:
                    if pile != []:
                        raise GobbletError(
                            "Une pile doit être une liste de deux entiers ou une liste vide")
        if len(gobelets) != 3:
            raise GobbletError("Le joueur doit possèder 3 piles")

        new = []  # Remplacer une liste vide par None dans gobelets
        for z in gobelets:
            if z == []:
                new.append(None)
            else:
                new.append(Gobblet(z[1], z[0]))
        return (nom, no_joueur, new)

    def __str__(self):
        """Formater un joueur.

        Returns:
            str: Représentation du joueur et de ses piles de gobelets.
        """
        temporary = f"{self.nom}: "
        x = 0
        for i in self.piles:
            if 0 < x < 3:
                temporary += " "
            x += 1
            if i is None:
                temporary += "   "
            else:
                temporary += i.__str__()
        return temporary

    def retirer_gobblet(self, no_pile):
        """Retirer un gobelet de la pile.

        Args:
            no_pile (int): le numéro de la pile [0, 1, 2].

        Returns:
            Gobblet: le gobelet retiré de la pile.

        Raises:
            GobbletError: Le numéro de la pile doit être un entier.
            GobbletError: Le numéro de la pile doit être 0, 1 ou 2.
            GobbletError: Le joueur ne possède pas de gobelet pour la pile demandée.
        """
        if isinstance(no_pile, int) is False:
            raise GobbletError("Le numéro de la pile doit être un entier")
        if no_pile not in [0, 1, 2]:
            raise GobbletError("Le numéro de la pile doit être 0, 1 ou 2")
        if self.piles[no_pile] is None:
            raise GobbletError(
                "Le joueur ne possède pas de gobelet pour la pile demandée")
        return self.piles[no_pile]
    # and self.piles.remove(self.piles[no_pile])

    def placer_gobblet(self, no_pile, gobelets):
        """Placer un gobelet dans la pile.

        Notez que les règles du jeu ne permettent pas de placer un gobelet dans une pile,
        sauf au début de la partie pour l'initialiser.

        L'emplacement de la pile doit donc être libre (valeur `None`).

        Args:
            no_pile (int): le numéro de la pile [0, 1, 2].
            gobelets (Gobblet): le gobelet à placer dans la pile.

        Raises:
            GobbletError: Le numéro de la pile doit être un entier.
            GobbletError: Le numéro de la pile doit être 0, 1 ou 2.
            GobbletError: Le gobelet doit appartenir au joueur.
            GobbletError: Vous ne pouvez pas placer un gobelet à cet emplacement.
        """
        if isinstance(no_pile, int) is False:
            raise GobbletError("Le numéro de la pile doit être un entier")
        if no_pile not in [0, 1, 2]:
            raise GobbletError("Le numéro de la pile doit être 0, 1 ou 2")
        if self.no_joueur != gobelets.no_joueur:
            raise GobbletError(
                "Le gobelet doit appartenir au joueur")
        if self.piles[no_pile] is not None:
            raise GobbletError(
                "Vous ne pouvez pas placer un gobelet à cet emplacement")
        self.piles[no_pile] = gobelets

    def récupérer_le_coup(self, plateau):
        """Récupérer le coup

        Demande au joueur le coup à jouer.
        Cette méthode ne doit PAS modifier le plateau.
        Cette méthode ne doit PAS modifier les piles de Gobblets.

        Returns:
            tuple: Un tuple composé d'une origine et de la destination.
                L'origine est soit un entier représentant le numéro de la pile du joueur
                ou une liste de 2 entier [x, y] représentant le gobelet sur le plateau.
                La destination est une liste de 2 entiers [x, y] représentant le gobelet
                sur le plateau.

        Raises:
            GobbletError: L'origine doit être un entier ou une liste de 2 entiers.
            GobbletError: L'origine n'est pas une pile valide.
            GobbletError: L'origine n'est pas une case valide du plateau.
            GobbletError: L'origine ne possède pas de gobelet.
            GobbletError: Le gobelet d'origine n'appartient pas au joueur.
            GobbletError: La destination doit être une liste de 2 entiers.
            GobbletError: La destination n'est pas une case valide du plateau.

        Examples:
            Quel gobelet voulez-vous déplacer:
            Donnez le numéro de la pile (p) ou la position sur le plateau (x,y): 0
            Où voulez-vous placer votre gobelet (x,y): 0,1

            Quel Gobbgobeletlet voulez-vous déplacer:
            Donnez le numéro de la pile (p) ou la position sur le plateau (x,y): 2,3
            Où voulez-vous placer votre gobelet (x,y): 0,1
        """
        print('Quel gobelet voulez-vous déplacer:')
        origin = input(
            'Donnez le numéro de la pile (p) ou la position sur le plateau (x,y):')
        destination = input('Où voulez-vous placer votre gobelet (x,y):')
        if len(origin) != 1:
            if isinstance(origin[0], str) or isinstance(origin[-2], str):
                raise GobbletError(
                    "L'origine doit être un entier ou une liste de 2 entiers")
            if isinstance(int(origin[0]), int) is False \
                    and isinstance(int(origin[-1]), int) is False:
                raise GobbletError(
                    "L'origine doit être un entier ou une liste de 2 entiers")
            if int(origin[0]) not in [0, 1, 2, 3] and int(origin[-1]) not in [0, 1, 2, 3]:
                raise GobbletError(
                    "L'origine n'est pas une case valide du plateau")
            if isinstance(plateau.plateau[int(origin[0])][int(origin[-1])][-1], Gobblet) and \
                    plateau.plateau[int(origin[0])][int(origin[-1])][-1].no_joueur != self.no_joueur:
                raise GobbletError(
                    "Le gobelet d'origine n'appartient pas au joueur")
            if type(plateau.plateau[int(origin[0])][int(origin[-1])][-1]) is False:
                raise GobbletError(
                    "L'origine ne possède pas de gobelet")
            origin = [int(origin[0]), int(origin[-1])]
        else:
            if origin.isdigit() is False:
                raise GobbletError(
                    "L'origine doit être un entier ou une liste de 2 entiers")
            origin = int(origin)
            if origin not in [0, 1, 2] or origin in [-1, -2]:
                raise GobbletError("L'origine n'est pas une pile valide")
            if isinstance(self.piles[origin], Gobblet) is False:
                raise GobbletError("L'origine ne possède pas de gobelet")
        if int(destination[0]) not in (0, 1, 2, 3) or int(destination[-1]) not in (0, 1, 2, 3):
            raise GobbletError(
                "La destination n'est pas une case valide du plateau")
        if len(destination) != 3 or isinstance(int(destination[0]), int) is False \
                or isinstance(int(destination[-1]), int) is False:
            raise GobbletError(
                "La destination doit être une liste de 2 entiers")
        destination = [int(destination[0]), int(destination[-1])]
        return (origin, destination)

    def état_joueur(self):
        """Obtenir l'état du joueur

        Returns:
            dict: Dictionnaire contenant l'état du joueur tel que représenté dans l'énoncé
        """
        liste = []
        for i in self.piles:
            if i is None:
                liste.append([])
            else:
                liste.append(i.état_gobblet())
        return {"nom": self.nom, "piles": liste}


class Automate(Joueur):
    def récupérer_le_coup(self, plateau):
        if len(self.piles) != 0:
            for i in range(4):
                for y in range(4):
                    if plateau[i, y] == []:
                        for b, _ in enumerate(self.piles):
                            return (b, [i, y])
                    else:
                        for o, b in enumerate(self.piles):
                            if plateau[i, y][-1].grosseur < b.grosseur:
                                return (o, [i, y])
        else:
            couple = []
            for i in range(4):
                for y in range(4):
                    if plateau[i, y] != []:
                        if plateau[i, y][-1].no_joueur == self.no_joueur:
                            couple.append([i, y])
                            couple.append(plateau[i, y][-1].grosseur)
            for a in range(4):
                for b in range(4):
                    if plateau[a, b][-1].grosseur < couple[1]:
                        return(couple[0], [a, b])

    def check_win(self, plateau):
        pass
