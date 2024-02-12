# >>> CONTRÔLEURS ---
# >>> TESTS ---
__TEST_TOUT_ACTIVER__: 							str = '__TEST_TOUT_ACTIVER__'
__TEST_PRECONDITION__: 							str = '__TEST_PRECONDITION__'
__TEST_CHARGER_CONTENU__: 						str = '__TEST_CHARGER_CONTENU__'
__TEST_AJOUTER_CARACTERES_DICO__: 				str = '__TEST_AJOUTER_CARACTERES_DICO__'
__TEST_AJOUTER_CODES_MORTS_DICO__: 				str = '__TEST_AJOUTER_CODES_MORTS_DICO__'
__TEST_AJOUTER_FONCTIONS_ASM_DICO__: 			str = '__TEST_AJOUTER_FONCTIONS_ASM_DICO__'
__TEST_AJOUTER_AUTRES_SYMBOLES_DICO__: 			str = '__TEST_AJOUTER_AUTRES_SYMBOLES_DICO__'
__TEST_CREER_DICTIONNAIRE__: 					str = '__TEST_CREER_DICTIONNAIRE__'
__TEST_CALCULER_LONGUEUR_CLEFS_DICTIONNAIRE__: 	str = '__TEST_CALCULER_LONGUEUR_CLEFS_DICTIONNAIRE__'
__TEST_TRANSPILATION__:							str = '__TEST_TRANSPILATION__'
__TEST_OBFUSQUER_CONTENU__:						str = '__TEST_OBFUSQUER_CONTENU__'
__TEST_INVERSER_DICTIONNAIRE__:					str = '__TEST_INVERSER_DICTIONNAIRE__'
__TEST_OBFUSCATION__:							str = '__TEST_OBFUSCATION__'
# --- TESTS <<<

# >>> ACTIVATION DES TESTS ---
__ACTIVATION_TESTS__: dict = {
    __TEST_TOUT_ACTIVER__: 							True,
    __TEST_PRECONDITION__: 							False,  # Cette ligne ne devrait pas être touchée
    __TEST_CHARGER_CONTENU__: 						False,
    __TEST_AJOUTER_CARACTERES_DICO__: 				False,
    __TEST_AJOUTER_CODES_MORTS_DICO__: 				False,
    __TEST_AJOUTER_FONCTIONS_ASM_DICO__: 			False,
    __TEST_AJOUTER_AUTRES_SYMBOLES_DICO__: 			False,
    __TEST_CREER_DICTIONNAIRE__: 					False,
    __TEST_CALCULER_LONGUEUR_CLEFS_DICTIONNAIRE__: 	False,
    __TEST_TRANSPILATION__:							False,
    __TEST_OBFUSQUER_CONTENU__:						False,
    __TEST_INVERSER_DICTIONNAIRE__:					False,
    __TEST_OBFUSCATION__:                           False,
}
# --- ACTIVATION DES TESTS <<<
