import string


# >>> CONSTANTES ---
CONSTANTES: dict = {
    'GLOBALES': {
        'FICHIER_MODE_LECTURE':   'r',
        'FICHIER_MODE_ECRITURE':  'w',
    },
    'AJOUTER_CARACTERES_DICO': {
        'LETTRES':    string.ascii_letters,
        'CHIFFRES':   string.digits,
        'SYMBOLES':   '()." /=:;<>_-\\+,\'{}#*[]',
        'PREFIXE':    '//[',
        'SUFFIXE':    ']'
    },
    'AJOUTER_CODES_MORTS_DICO': {
        'CODES_MORTS': ['//[0x7F]',
                        '//[0x00]',
                        '//[0x07]',
                        '//[0x1E]']
    },
    'AJOUTER_FONCTIONS_ASM_DICO': {
        'FONCTIONS_ASM':  ['if',
                           'else',
                           'while',
                           'for',
                           'range',
                           'try'],
        'PREFIXE':         '_ZN4crtl1',
        'SUFFIXE':        'C1Ev',
    },
    'AJOUTER_AUTRES_SYMBOLES_DICO': {
        'AUTRES_SYMBOLES': {
            '_ZN4crtl2exC1Ev': 'except',
            '_ZN4util3impC1Ev': 'import',
            '//[0x09]': '\n',
        }
    },
    'CHEMINS': {
        'BRUMEUX':        'programme-obfusque.txt',
        'TRANSPILE':      'programme-decouvert.txt',
        'A_OBFUSQUER':    'programme-a-obfusquer.txt',
        'OBFUSQUE':       'programme-obfusque.txt',
    }
}
# <<< CONSTANTES ---
