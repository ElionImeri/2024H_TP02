import assets.constants.constants as __CST__


__version__ = "TP2 - Exercice 'Dans la brume...'"
__author__ = "Nom élève 1 (matricule 1), nom élève 2 (matricule 2)"


"""
 * <1.0> charger_contenu
 * Charge le contenu d'un fichier texte en mode lecture à partir du chemin d'un fichier.
 * @param   chemin_fichier  (str) Le chemin vers le fichier à lire.
 * @return                  (str) Le contenu du fichier lu.
"""


def charger_contenu(chemin_fichier: str) -> str:
    with open(chemin_fichier,
              __CST__.CONSTANTES['GLOBALES']['FICHIER_MODE_LECTURE']) as fichier_brumeux:
        return fichier_brumeux.read()


"""
 * <2.0.> ajouter_caracteres
 * Ajoute uniquement les caractères (lettres, chiffres et autres symboles) au dictionnaire.
 * @param dictionnaire  (dict) Le dictionnaire.
 * @return              (dict) Le dictionnaire mis à jour avec les nouvelles clefs.
"""


def ajouter_caracteres_dico(dictionnaire: dict) -> dict:
    prefixe = __CST__.CONSTANTES['AJOUTER_CARACTERES_DICO']['PREFIXE']
    suffixe = __CST__.CONSTANTES['AJOUTER_CARACTERES_DICO']['SUFFIXE']
    lettres = __CST__.CONSTANTES['AJOUTER_CARACTERES_DICO']['LETTRES']
    chiffres = __CST__.CONSTANTES['AJOUTER_CARACTERES_DICO']['CHIFFRES']
    symboles = __CST__.CONSTANTES['AJOUTER_CARACTERES_DICO']['SYMBOLES']
    
    for x in lettres + chiffres + symboles: # TODO Parcourir les lettres, chiffres et symboles à ajouter au dictionnaire
        dictionnaire[prefixe + x + suffixe] = hex(ord(x)) # TODO Ajouter le préfixe et le suffixe au caractère parcouru au sein de votre dictionnaire

    return dictionnaire


"""
 * <2.1.> ajouter_codes_morts_dico
 * Ajoute uniquement les codes morts au dictionnaire.
 * @param dictionnaire  (dict) Le dictionnaire.
 * @return              (dict) Le dictionnaire mis à jour avec les nouvelles clefs.
"""


def ajouter_codes_morts_dico(dictionnaire: dict) -> dict:
    codes_morts = __CST__.CONSTANTES['AJOUTER_CODES_MORTS_DICO']['CODES_MORTS']

    for valeur in codes_morts: # TODO Similairement à 2.0, ajouter les codes morts à votre dictionnaire
        dictionnaire[valeur] = valeur, codes_morts

    return dictionnaire


"""
 * <2.2.> ajouter_fonctions_asm_dico
 * Ajoute uniquement les fonctions d'assembleur (_ZNxxx) au dictionnaire.
 * @param dictionnaire  (dict) Le dictionnaire.
 * @return              (dict) Le dictionnaire mis à jour avec les nouvelles clefs.
"""


def ajouter_fonctions_asm_dico(dictionnaire: dict) -> dict:
    prefixe = __CST__.CONSTANTES['AJOUTER_FONCTIONS_ASM_DICO']['PREFIXE']  # TODO Ajouter cette constante pour les codes en assembleur
    suffixe = __CST__.CONSTANTES['AJOUTER_FONCTIONS_ASM_DICO']['SUFFIXE']  # TODO Ajouter cette constante pour les codes en assembleur
    symboles = __CST__.CONSTANTES['AJOUTER_CARACTERES_DICO']['SYMBOLES']
    fonctions_asm = __CST__.CONSTANTES['AJOUTER_FONCTIONS_ASM_DICO']['FONCTIONS_ASM']

    for valeur in prefixe + suffixe + symboles: # TODO Parcourir les lettres, chiffres et symboles à ajouter au dictionnaire
        for element in fonctions_asm: # TODO Ajouter le préfixe et le suffixe au caractère assembleur parcouru au sein de votre dictionnaire
            dictionnaire[prefixe + element + suffixe] = element

    return dictionnaire


"""
 * <2.3.> ajouter_autres_symboles_dico
 * Ajoute uniquement tout autre symbole n'ayant pas encore été ajouté au dictionnaire.
 * @param dictionnaire  (dict) Le dictionnaire.
 * @return              (dict) Le dictionnaire mis à jour avec les dernières clefs.
"""


def ajouter_autres_symboles_dico(dictionnaire: dict) -> dict:
    autres_symboles = __CST__.CONSTANTES['AJOUTER_AUTRES_SYMBOLES_DICO']['AUTRES_SYMBOLES']

    for element in autres_symboles.items(): # TODO Mettre à jour le dictionnaire avec les autres symboles
        dictionnaire[element] = autres_symboles

    return dictionnaire


"""
 * <2.4.> creer_dictionnaire
 * Appel en chaîne à vos fonctions définies plus haut pour créer le dictionnaire final.
 * @return (dict) Votre dictionnaire complet.
"""


def creer_dictionnaire() -> dict:
    # Initialisation du dictionnaire
    dictionnaire: dict = dict()

    # TODO Ajouter les caractères au dictionnaire (appel de votre fonction)
    dictionnaire = ajouter_caracteres_dico(dictionnaire)

    # TODO Ajouter les codes morts au dictionnaire (appel de votre fonction)
    dictionnaire = ajouter_codes_morts_dico(dictionnaire)

    # TODO Ajouter les fonctions assembleur au dictionnaire (appel de votre fonction)
    dictionnaire = ajouter_fonctions_asm_dico(dictionnaire)

    # TODO Ajouter les autres symboles au dictionnaire (appel de votre fonction)
    dictionnaire = ajouter_autres_symboles_dico(dictionnaire)

    return dictionnaire


"""
 * <3.0.> calculer_longueur_clefs_dictionnaire
 * Crée un ensemble de toutes les longueurs des clefs du dictionnaire.
 * @param   dictionnaire    (dict)      Le dictionnaire en question.
 * @return                  (set[int])  L'ensemble des longueurs des clefs du dictionnaire.
"""


def calculer_longueur_clefs_dictionnaire(dictionnaire: dict) -> set[int]:
    possibilites_longueur: set[int] = set()

    for key in dictionnaire: # TODO Parcourir toutes les clefs du dictionnaire et ajouter leurs longueurs à possibilites_longueur
        possibilites_longueur.add(len(key))

    return possibilites_longueur


"""
 * <3.1.> transpiler
 * Transpile un programme brumeux en un programme à découvert.
 * Vous devez parcourir l'ensemble des possibilités des longueurs des clefs de votre
 * dictionnaire à l'envers, et remplacer itérativement tous les caractères et mnémoniques 
 * du programme brumeux vers un programme transpilé (à découvert).
 * @param   programme_brumeux       (str)       Le programme brumeux à transpiler.
 * @param   possibilites_longueur   (set[int])  L'ensemble longueurs des clefs du dictionnaire.
 * @param   dictionnaire            (dict)      Votre dictionnaire.
 * @return                          (str)       Le programme transpilé à découvert.
"""


def transpiler(programme_brumeux:       str,
               possibilites_longueur:   set[int],
               dictionnaire:            dict) -> str:

    programme_decouvert: str = ''

    # TODO: Référez-vous au pseudo-code fourni dans le fichier texte 'pseudo_code.txt'

    return programme_decouvert


"""
 * <3.2.> ecriture_programme_transpile
 * Écriture de votre programme transpilé au sein d'un fichier texte.
 * @param   chemin_fichier_transpile    (str)   Le chemin de sortie vers votre fichier transpilé.
 * @param   programme_decouvert         (str)   Le programme à écrire.
"""


def ecriture_programme_transpile(chemin_fichier_transpile:  str,
                                 programme_decouvert:       str) -> None:
    with open(chemin_fichier_transpile, __CST__.CONSTANTES['GLOBALES']['FICHIER_MODE_ECRITURE']) as fichier_transpile:
        fichier_transpile.write(programme_decouvert)


"""
 * <3.3.> transpilation
 * Appels successifs à vos fonctions écrites précédemment pour exécuter la transpilation.
 * @param chemin_fichier_brumeux    (str) Le chemin vers le fichier brumeux.    [defined by default]
 * @param chemin_fichier_transpile  (str) Le chemin vers le fichier transpilé.  [defined by default]
"""


def transpilation(chemin_fichier_brumeux:   str = __CST__.CONSTANTES['CHEMINS']['BRUMEUX'],
                  chemin_fichier_transpile: str = __CST__.CONSTANTES['CHEMINS']['TRANSPILE']) -> None:

    # TODO Charger le contenu du programme brumeux (appel de votre fonction)
    # programme_brumeux: str = charger_contenu(chemin_fichier_brumeux)

    # TODO Création du dictionnaire (appel de votre fonction)
    # dictionnaire: dict = ...
    dictionnaire = ...

    # TODO Calculer les longueurs des clefs de votre dictionnaire (appel de votre fonction)
    possibilites_longueur: set = calculer_longueur_clefs_dictionnaire(
        dictionnaire)

    # TODO Effectuer la transpilation de votre programme brumeux en un programme à découvert (appel de votre fonction)
    programme_decouvert: str = ...

    # TODO Écrire votre programme transpilé dans un fichier texte (appel de votre fonction)

    # --- Ne pas modifier ce qui suit ---
    if __name__ == "__main__":
        print(f'Transpilation terminee avec succes du fichier {chemin_fichier_brumeux} au sein du fichier'
              f' {chemin_fichier_transpile}')


"""
 * <4.0.> obfusquer_contenu
 * Obfusque le contenu à partir de votre dictionnaire inversé.
 * @param   contenu_a_obfusquer     (str)   Le contenu à obfusquer.
 * @param   dictionnaire_inverse    (dict)  Votre dictionnaire inversé.
 * @return                          (str)   Le contenu obfusqué.
"""


def obfusquer_contenu(contenu_a_obfusquer:  str,
                      dictionnaire_inverse: dict) -> str:
    contenu_obfusque: str = ''

    # TODO Parcourir chaque lettre au sein du contenu à obfusquer
    # TODO Ajouter la valeur de votre dictionnaire inversé (la lettre étant la clef) à votre contenu obfusqué

    return contenu_obfusque


"""
 * <4.1.> ecrire_contenu_obfusque
 * Écrire le contenu obfusqué au sein d'un fichier texte.
 * @param   chemin_fichier_obfusque (str)   Le chemin dudit fichier texte.
 * @param   contenu_obfusque        (str)   Votre dictionnaire inversé.
 * @param   mode                    (str)   Mode de l'ouverture du fichier en écriture. [defined by default]
"""


def ecrire_contenu_obfusque(chemin_fichier_obfusque:    str,
                            contenu_obfusque:           str,
                            mode:                       str =
                            __CST__.CONSTANTES['GLOBALES']['FICHIER_MODE_ECRITURE']) -> None:
    with open(chemin_fichier_obfusque, mode) as fichier_obfusque:
        fichier_obfusque.write(contenu_obfusque)


"""
 * <4.2.> inverser_dictionnaire
 * Inverse votre dictionnaire.
 * @param   dictionnaire_initial    (dict)  Votre dictionnaire initial.
 * @return                          (dict)  Votre dictionnaire inversé.
"""


def inverser_dictionnaire(dictionnaire_initial) -> dict:
    # TODO Inversez votre dictionnaire (clef: valeur -> valeur: clef) afin de créer un
    # dictionnaire permettant de faciliter l'obfuscation du contenu
    return dictionnaire_initial  # TODO Modifiez ceci


"""
 * <4.3.> obfuscation
 * Exécute les fonctions définies plus haut pour obfusquer un programme. 
 * @param chemin_fichier_a_obfusquer    (str) Le chemin vers le fichier à obfusquer.    [defined by default]
 * @param chemin_fichier_obfusque       (str) Le chemin vers le fichier obfusqué.       [defined by default]
"""


def obfuscation(chemin_fichier_a_obfusquer: str = __CST__.CONSTANTES['CHEMINS']['A_OBFUSQUER'],
                chemin_fichier_obfusque:    str = __CST__.CONSTANTES['CHEMINS']['OBFUSQUE']) -> None:
    # TODO Obtenir le contenu du fichier à obfusquer (appel de votre fonction)
    contenu_a_obfusquer: str = ...

    # TODO Création du dictionnaire initial comme pour la transpilation (appel de votre fonction)
    dictionnaire_initial: dict = ...

    # TODO Inversion du dictionnaire (appel de votre fonction)
    dictionnaire_inverse: dict = ...

    # TODO Obfusquer le contenu du dictionnaire (appel de votre fonction)
    contenu_obfusque: str = ...

    # TODO: Écriture du contenu obfusqué au sein d'un fichier texte (appel de votre fonction)

    # --- Ne pas modifier ce qui suit ---
    if __name__ == "__main__":
        print(f'Obfuscation terminée avec succès du fichier {chemin_fichier_a_obfusquer} au sein du fichier'
              f' {chemin_fichier_obfusque}')
