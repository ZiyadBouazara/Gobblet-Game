"""Module Joueur

Functions:
    * Joueur - Classe représentant un joueur de Gobblet.
"""

from gobblet import Gobblet, GobbletError


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
        self.nom, self.no_joueur, self.piles = self.valider_joueur(nom, no_joueur, gobelets)

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
        pass

    def __str__(self):
        """Formater un joueur.

        Returns:
            str: Représentation du joueur et de ses piles de gobelets.
        """
        pass

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
        pass

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
        pass

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
        pass

    def état_joueur(self):
        """Obtenir l'état du joueur

        Returns:
            dict: Dictionnaire contenant l'état du joueur tel que représenté dans l'énoncé
        """
        pass
