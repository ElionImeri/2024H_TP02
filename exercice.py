import assets.constants.constants as __CST__


__version__ = "TP2 - Exercice 'Dans la brume...'"
__author__ = "Johnny Jang (2215135), Elion Imeri (2332034)"


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
    suffixe = __CST__.CONSTANTES['AJOUTER_CARACTERES_DICO']['SUFFIXE']  # TODO Ajouter cette constante
    lettres = __CST__.CONSTANTES['AJOUTER_CARACTERES_DICO']['LETTRES']
    chiffres = __CST__.CONSTANTES['AJOUTER_CARACTERES_DICO']['CHIFFRES']
    symboles = __CST__.CONSTANTES['AJOUTER_CARACTERES_DICO']['SYMBOLES']
    # TODO Parcourir les lettres, chiffres et symboles à ajouter au dictionnaire
    for charactere in lettres + chiffres + symboles:
    # TODO Ajouter le préfixe et le suffixe au caractère parcouru au sein de votre dictionnaire
        hex_key = prefixe+hex(ord(charactere))+suffixe
        dictionnaire[hex_key] = charactere
    return dictionnaire


"""
 * <2.1.> ajouter_codes_morts_dico
 * Ajoute uniquement les codes morts au dictionnaire.
 * @param dictionnaire  (dict) Le dictionnaire.
 * @return              (dict) Le dictionnaire mis à jour avec les nouvelles clefs.
"""


def ajouter_codes_morts_dico(dictionnaire: dict) -> dict:
    # TODO Similairement à 2.0, ajouter les codes morts à votre dictionnaire
    codes_morts = __CST__.CONSTANTES['AJOUTER_CODES_MORTS_DICO']['CODES_MORTS']
    for charactere_mort in codes_morts:
        dictionnaire[charactere_mort] = ''
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
    asm = __CST__.CONSTANTES['AJOUTER_FONCTIONS_ASM_DICO']['FONCTIONS_ASM']
    # TODO Parcourir les lettres, chiffres et symboles à ajouter au dictionnaire -> PARCOURIR LES FONCTIONS ASSEMBLEUR
    abv_map = {
        'if': 'i',
        'else': 'e',
        'while': 'w',
        'for': 'f',
        'range': 'r',
        'try': 't',
        }

    for value in asm:
        abbreviation = abv_map.get(value, value)
        key = prefixe+abbreviation+suffixe
        dictionnaire[key] = value
        #print(f"key: {key}, value: {value}, vlaue type: {type(value)}") #debug

    return dictionnaire
"""
 * <2.3.> ajouter_autres_symboles_dico
 * Ajoute uniquement tout autre symbole n'ayant pas encore été ajouté au dictionnaire.
 * @param dictionnaire  (dict) Le dictionnaire.
 * @return              (dict) Le dictionnaire mis à jour avec les dernières clefs.
"""


def ajouter_autres_symboles_dico(dictionnaire: dict) -> dict:
    # TODO Mettre à jour le dictionnaire avec les autres symboles
    asm_symbole = __CST__.CONSTANTES['AJOUTER_AUTRES_SYMBOLES_DICO']['AUTRES_SYMBOLES']
    for character_asm, value in asm_symbole.items():
        dictionnaire[character_asm] = value
        #print(f"key: {character_asm}, value: {value}, value type: {type(value)}") #debug

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
    #print(dictionnaire) #debug
    return dictionnaire


"""
 * <3.0.> calculer_longueur_clefs_dictionnaire
 * Crée un ensemble de toutes les longueurs des clefs du dictionnaire.
 * @param   dictionnaire    (dict)      Le dictionnaire en question.
 * @return                  (set[int])  L'ensemble des longueurs des clefs du dictionnaire.
"""


def calculer_longueur_clefs_dictionnaire(dictionnaire: dict) -> set[int]:
    possibilites_longueur: set[int] = set()

    # TODO Parcourir toutes les clefs du dictionnaire et ajouter leurs longueurs à possibilites_longueur
    for cle in dictionnaire:
        possibilites_longueur.add(len(cle))
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
    i=0
    possibilites_triees = sorted(possibilites_longueur, reverse=True)
    
    # TODO: Référez-vous au pseudo-code fourni dans le fichier texte 'pseudo_code.txt'
    while i < len(programme_brumeux):
        for longueur in possibilites_triees:
            debut = i
            fin = i + longueur
            mot_asm = programme_brumeux[debut:fin] # pr extraire substring, use slcing [start:end]
            if mot_asm in dictionnaire:
                i +=longueur
                programme_decouvert += dictionnaire[mot_asm]
                break
    
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
    programme_brumeux: str = charger_contenu(chemin_fichier_brumeux)
    
    # TODO Création du dictionnaire (appel de votre fonction)
    # dictionnaire: dict = ...
    dictionnaire = creer_dictionnaire()
    
    # TODO Calculer les longueurs des clefs de votre dictionnaire (appel de votre fonction)
    possibilites_longueur: set = calculer_longueur_clefs_dictionnaire(dictionnaire)

    # TODO Effectuer la transpilation de votre programme brumeux en un programme à découvert (appel de votre fonction)
    programme_decouvert: str = transpiler(programme_brumeux, possibilites_longueur, dictionnaire)

    # TODO Écrire votre programme transpilé dans un fichier texte (appel de votre fonction)
    ecriture_programme_transpile(chemin_fichier_transpile, programme_decouvert)
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
    for lettre in contenu_a_obfusquer:
    # TODO Ajouter la valeur de votre dictionnaire inversé (la lettre étant la clef) à votre contenu obfusqué
        if lettre in dictionnaire_inverse:
            contenu_obfusque += dictionnaire_inverse[lettre]
        else:
            contenu_obfusque += lettre

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
    dictionnaire_inverse = {}
    for cle, valeur in dictionnaire_initial.items():
        dictionnaire_inverse[valeur] = cle
    return dictionnaire_inverse # TODO Modifiez ceci


"""
 * <4.3.> obfuscation
 * Exécute les fonctions définies plus haut pour obfusquer un programme. 
 * @param chemin_fichier_a_obfusquer    (str) Le chemin vers le fichier à obfusquer.    [defined by default]
 * @param chemin_fichier_obfusque       (str) Le chemin vers le fichier obfusqué.       [defined by default]
"""


def obfuscation(chemin_fichier_a_obfusquer: str = __CST__.CONSTANTES['CHEMINS']['A_OBFUSQUER'],
                chemin_fichier_obfusque:    str = __CST__.CONSTANTES['CHEMINS']['OBFUSQUE']) -> None:
    # TODO Obtenir le contenu du fichier à obfusquer (appel de votre fonction)
    contenu_a_obfusquer: str = charger_contenu(chemin_fichier_a_obfusquer)

    # TODO Création du dictionnaire initial comme pour la transpilation (appel de votre fonction)
    dictionnaire_initial: dict = creer_dictionnaire()

    # TODO Inversion du dictionnaire (appel de votre fonction)
    dictionnaire_inverse: dict = inverser_dictionnaire(dictionnaire_initial)

    # TODO Obfusquer le contenu du dictionnaire (appel de votre fonction)
    contenu_obfusque: str = obfusquer_contenu(contenu_a_obfusquer,dictionnaire_inverse)

    # TODO: Écriture du contenu obfusqué au sein d'un fichier texte (appel de votre fonction)
    ecrire_contenu_obfusque(chemin_fichier_obfusque,contenu_obfusque)
    # --- Ne pas modifier ce qui suit ---
    if __name__ == "__main__":
        print(f'Obfuscation terminée avec succès du fichier {chemin_fichier_a_obfusquer} au sein du fichier'
              f' {chemin_fichier_obfusque}')
