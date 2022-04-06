"""Module Joueur

Functions:
    * Plateau - Classe représentant un Plateau.
"""

from gobblet import Gobblet, GobbletError


class Plateau:
    """
    Plateau
    """

    def __init__(self, plateau):
        """Constructeur de Plateau

        Vous ne devez PAS modifier cette méthode

        Args:
            plateau (list): Plateau à construire tel que représenté dans l'énoncé
        """
        self.plateau = self.valider_plateau(plateau)

    def valider_plateau(self, plateau):
        """Validateur de Plateau

        Args:
            plateau (list): Plateau tel que représenté dans l'énoncé

        Returns:
            list: Plateau composé de liste de Gobblets ou None pour l'absence de Gobblet

        Raises:
            GobbletError: Le plateau doit être une liste
            GobbletError: Le plateau ne possède pas le bon nombre de ligne
            GobbletError: Le plateau ne possède pas le bon nombre de colonne dans les lignes
            GobbletError: Les Gobblets doivent être des listes de paires ou une liste vide
        """
        # INCOMPLET
        if type(plateau) != list:
            raise GobbletError('Le plateau doit être une liste')
        if len(plateau) != 4:
            raise GobbletError('Le plateau ne possède pas le bon nombre de ligne')
        for i in range(5):
            if len(plateau[i]) != 4:
                raise GobbletError('Le plateau ne possède pas le bon nombre de colonne dans les lignes')
            for n in range(3):
                if len(plateau[i][n]) != [] or len(plateau[i][n]) != 2:
                    raise GobbletError('Les Gobblets doivent être des listes de paires ou une liste vide')
                if len(plateau[i][n]) == []: #À MODIFIER
                    return None
        return (plateau)

    def __str__(self):
        """Formater un plateau

        Returns:
            str: Représentation du plateau avec ses Gobblet
        """
        plateau = ""
        for i in range(4):
            #On établie et formate les 4 gobblets respectifs a chaque ligne
            gobblet = [(self[i][0]).__str__(), (self[i][1]).__str__(), (self[i][2]).__str__(), (self[i][3]).__str__()]
            plateau += f"{3-i}{gobblet[0]}|{gobblet[1]}|{gobblet[2]}|{gobblet[3]}\n"
            if 3-i != 0:
                plateau += " ───┼───┼───┼───\n"
            else:
                plateau += "  0   1   2   3 "
        return plateau

    def retirer_gobblet(self, no_colonne, no_ligne):
        """Retirer un Gobblet du plateau

        Args:
            no_colonne (int): Numéro de la colonne
            no_ligne (int): Numéro de la ligne

        Returns:
            Gobblet: Gobblet retiré du plateau

        Raises:
            GobbletError: Ligne et colonne doivent être des entiers
            GobbletError: Le numéro de la ligne doit être 0, 1, 2 ou 3
            GobbletError: Le numéro de la colonne doit être 0, 1, 2 ou 3
            GobbletError: Le plateau ne possède pas de Gobblet pour la case demandée
        """
        # J'accède à l'information pour formater le gobblet
        gobblet_retiré =  self[no_ligne][no_colonne]
        # Comment je retourne la version formatée du gobblet? Pas certaine de ce que j'ai fait.
        gobblet_formaté = gobblet_retiré.__str__()
        
        # Errors
        if type(no_colonne) != list or type(no_ligne) != list:
            raise GobbletError('Ligne et colonne doivent être des entiers')
        if no_ligne not in (0, 1, 2, 3):
            raise GobbletError('Le numéro de la ligne doit être 0, 1, 2 ou 3')
        if no_colonne not in (0, 1, 2, 3):
            raise GobbletError('Le numéro de la colonne doit être 0, 1, 2 ou 3')
        if self.plateau[no_ligne][no_colonne] == []:
            raise GobbletError('Le plateau ne possède pas de Gobblet pour la case demandée')
    
        return gobblet_formaté

    def placer_gobblet(self, no_colonne, no_ligne, gobblet):
        """Placer un Gobblet dans le plateau

        Args:
            no_colonne (int): Numéro de la colonne (0, 1, 2 ou 3)
            no_ligne (int): Numéro de la ligne (0, 1, 2 ou 3)
            gobblet (Gobblet): Gobblet à placer dans le plateau

        Raises:
            GobbletError: Ligne et colonne doivent être des entiers
            GobbletError: Le numéro de la ligne doit être 0, 1, 2 ou 3
            GobbletError: Le numéro de la colonne doit être 0, 1, 2 ou 3
            GobbletError: Le Gobblet ne peut pas être placé sur la case demandée
        """
        # Incomplet! Comment coder ce qui est demandé?
        self.plateau[no_ligne][no_colonne] == gobblet

        # J'ai seulement fait les Errors
        if type(no_colonne) != list or type(no_ligne) != list:
            raise GobbletError('Ligne et colonne doivent être des entiers')
        if no_ligne not in (0, 1, 2, 3):
            raise GobbletError('Le numéro de la ligne doit être 0, 1, 2 ou 3')
        if no_colonne not in (0, 1, 2, 3):
            raise GobbletError('Le numéro de la colonne doit être 0, 1, 2 ou 3')
        if self.plateau[no_ligne][no_colonne] is not None and self.plateau[no_ligne][no_colonne][0] >= gobblet[0]:
            raise GobbletError('Le Gobblet ne peut pas être placé sur la case demandée')

    def état_plateau(self):
        """Obtenir l'état du plateau

        Returns:
            list: Liste contenant l'état du plateau tel que représenté dans l'énoncé
        """
        return [self.plateau]
