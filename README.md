# TP2 : Dans la brume...

![TP2](./assets/cover.webp)

<p align="left"> <i>Crédits: <a href="https://openai.com/blog/dall-e/">DALLE 3</a></i></p>

## Table des matières

- [TP2 : Dans la brume...](#tp2--dans-la-brume)
  - [Table des matières](#table-des-matières)
  - [⏰ Date de remise: le dimanche 3 mars 23h59.](#-date-de-remise-le-dimanche-3-mars-23h59)
  - [Introduction](#introduction)
  - [Objectifs](#objectifs)
  - [Description](#description)
    - [Partie 1. Transpilation](#partie-1-transpilation)
      - [Question bonie (1 point)](#question-bonie-1-point)
        - [**Attention !** Ne convertissez en aucun cas ce programme (.txt) en fichier exécutable (.py) !](#attention--ne-convertissez-en-aucun-cas-ce-programme-txt-en-fichier-exécutable-py-)
    - [Partie 2. Obfuscation](#partie-2-obfuscation)
  - [Exécution des tests unitaires](#exécution-des-tests-unitaires)
  - [Remise](#remise)
  - [Barème](#barème)

## ⏰ Date de remise: le dimanche 3 mars 23h59.

## Introduction

Bienvenue dans ce défi de programmation Python centré sur la sécurité informatique et le décryptage. Votre mission est de plonger au cœur d'un ransomware, en analysant et en déjouant ses mécanismes de cryptage. Ce travail vous amènera à endosser le rôle d'un cyber-détective, employant vos compétences en programmation pour percer les secrets d'un système de conversion de caractères complexe utilisé par les cybercriminels.

## Objectifs

- Maîtriser les listes et dictionnaires pour l'organisation de données complexes.

- Apprendre à gérer des fichiers texte, essentiels pour manipuler des données persistantes.

- Écrire des fonctions réutilisables pour améliorer la lisibilité, la modularité, et l'efficacité du code.

- Appliquer la connaissance du code ASCII dans le traitement de texte et la conversion de caractères.

## Description

Étant expert en sécurité informatique, la firme **Skynet** vous engage en tant que consultant pour déceler l'impact des plus récentes attaques sur leur serveur Jira. Ingénieur.e en devenir, vous usez de vos plus récentes connaissances _pythoniques_ en manipulation de fonctions et de fichiers pour trouver la cible des cybercriminels.

Dans leur plus récent rapport, **Skynet** a affirmé que les pirates n'ont pas pu effacer complètement les traces de leur méfait. À vrai dire, les administrateurs réseaux de la firme ont pu intercepter un des programmes utilisés par les pirates pendant leur attaque, qui vous est remis sous le nom de **`programme-brumeux.txt`**.

Néanmoins, les pirates ont prévu qu'une telle fuite pourrait survenir. Ainsi, le code source a été **obfusqué**; toutes les fonctions, structures de contrôle et noms de variable ont été substitués et obscurcis par des caractères incrompréhensibles. Heureusement, grâce à une analyse des fréquences, l'équipe **Skynet** a pu dresser ce tableau de correspondance, dont la majorité figurent en assembleur (_asm_) et en _ASCII_:

**Tableau 1.** Équivalences compréhensibles des structures de contrôle et divers caractères obfusqués.

| Code obfusqué     | Équivalence en Python                         |
| ----------------- | --------------------------------------------- |
| \_ZN4crtl1iC1Ev   | if                                            |
| \_ZN4crtl1eC1Ev   | else                                          |
| \_ZN4crtl1wC1Ev   | while                                         |
| \_ZN4crtl1fC1Ev   | for                                           |
| \_ZN4crtl1rC1Ev   | range                                         |
| \_ZN4crtl1tC1Ev   | try                                           |
| \_ZN4crtl2exC1Ev  | except                                        |
| \_ZN4util3impC1Ev | import                                        |
| //[0x28]          | (                                             |
| //[0x23]          | #                                             |
| //[0x29]          | )                                             |
| //[0x2e]          | .                                             |
| //[0x34]          | "                                             |
| //[0x27]          | '                                             |
| //[0x20]          | [ESPACE]                                      |
| //[0x57]          | /                                             |
| //[0x3d]          | =                                             |
| //[0x3a]          | :                                             |
| //[0x3b]          | ;                                             |
| //[0x3c]          | <                                             |
| //[0x3e]          | >                                             |
| //[0x5f]          | \_                                            |
| //[0x2d]          | -                                             |
| //[0x5c]          | \|                                            |
| //[0x2b]          | +                                             |
| //[0x2c]          | ,                                             |
| //[0x61]          | a                                             |
| //[0x62]          | b                                             |
| //[0x63]          | c                                             |
| //[0x64]          | d                                             |
| //[0x65]          | e                                             |
| //[0x66]          | f                                             |
| //[0x67]          | g                                             |
| //[0x68]          | h                                             |
| //[0x69]          | i                                             |
| //[0x6a]          | j                                             |
| //[0x6b]          | k                                             |
| //[0x6c]          | l                                             |
| //[0x6d]          | m                                             |
| //[0x6e]          | n                                             |
| //[0x6f]          | o                                             |
| //[0x70]          | p                                             |
| //[0x71]          | q                                             |
| //[0x72]          | r                                             |
| //[0x73]          | s                                             |
| //[0x74]          | t                                             |
| //[0x75]          | u                                             |
| //[0x76]          | v                                             |
| //[0x77]          | w                                             |
| //[0x78]          | x                                             |
| //[0x79]          | y                                             |
| //[0x7a]          | z                                             |
| //[0x41]          | A                                             |
| //[0x42]          | B                                             |
| //[0x43]          | C                                             |
| //[0x44]          | D                                             |
| //[0x45]          | E                                             |
| //[0x46]          | F                                             |
| //[0x47]          | G                                             |
| //[0x48]          | H                                             |
| //[0x49]          | I                                             |
| //[0x4a]          | J                                             |
| //[0x4b]          | K                                             |
| //[0x4c]          | L                                             |
| //[0x4d]          | M                                             |
| //[0x4e]          | N                                             |
| //[0x4f]          | O                                             |
| //[0x50]          | P                                             |
| //[0x51]          | Q                                             |
| //[0x52]          | R                                             |
| //[0x53]          | S                                             |
| //[0x54]          | T                                             |
| //[0x55]          | U                                             |
| //[0x56]          | V                                             |
| //[0x57]          | W                                             |
| //[0x58]          | X                                             |
| //[0x59]          | Y                                             |
| //[0x5a]          | Z                                             |
| //[0x7f]          | [CODE MORT -- À REMPLACER PAR LA CHAÎNE VIDE] |
| //[0x00]          | [CODE MORT -- À REMPLACER PAR LA CHAÎNE VIDE] |
| //[0x07]          | [CODE MORT -- À REMPLACER PAR LA CHAÎNE VIDE] |
| //[0x1e]          | [CODE MORT -- À REMPLACER PAR LA CHAÎNE VIDE] |
| //[0x30]          | 0                                             |
| //[0x31]          | 1                                             |
| //[0x32]          | 2                                             |
| //[0x33]          | 3                                             |
| //[0x34]          | 4                                             |
| //[0x35]          | 5                                             |
| //[0x36]          | 6                                             |
| //[0x37]          | 7                                             |
| //[0x38]          | 8                                             |
| //[0x39]          | 9                                             |
| //[0x7b]          | {                                             |
| //[0x7d]          | }                                             |
| //[0x5b]          | [                                             |
| //[0x5c]          | ]                                             |
| //[0x09]          | \n                                            |
| //[0x2a]          | \*                                            |

### Partie 1. Transpilation

- Convertir le fichier **`programme-brumeux.txt`** en fichier compréhensible pour y comprendre le fonctionnement derrière l'attaque des cybercriminels.
- Votre conversion devrait créer un second fichier, nommé **`programme-decouvert.txt`**, qui contiendra le code transpilé à partir du **Tableau 1**. **Il est à noter que vous ne devriez pas copier, à la main, l'entièreté de ce tableau pour la création de votre dictionnaire.** Il est fourni à titre de référence. Référez-vous plutôt aux constantes du premier exercice.
- Votre programme de transpilation devrait fonctionner pour tous les autres virus qui seront potentiellement découverts par **Skynet**, et non seulement pour le **`programme-brumeux.txt`**. Laissez-vous guider par les instructions incluses au sein du fichier **`exercice1.py`** pour arriver à vos fins.

#### Question bonie (1 point)

- Écrivez une description précise de l'exécution du programme utilisé par les pirates lors de l'attaque, selon le code transpilé à l'exercice 1. Cette description devrait figurer au sein du fichier **`boni.txt`**.

##### **Attention !** Ne convertissez en aucun cas ce programme (.txt) en fichier exécutable (.py) !

### Partie 2. Obfuscation

- La firme **Skynet** en a assez de se faire larguer des virus par des cybercriminels ! Elle décide ainsi de contre-attaquer ! Quoi de mieux que de combattre le feu par le feu !
- Vous devez développer une fonction qui permet d'obfusquer n'importe quel programme de la firme dans le but de combattre les malfaiteurs. Laissez-vous guider par les instructions includes au sein du fichier **`exercice1.py`** pour arriver à vos fins.
- Dans le cadre de cet exercice, vous devrez obfusquer le **`programme-a-obfusquer.txt`** au sein du fichier **`programme-obfusque.txt`**.

## Exécution des tests unitaires

- Pour tester votre programme, une suite de tests est mise à votre disposition au sein de **`test-exercice.py`**.

- Pour vous aider à tester individuellement les fonctions, nous vous fournissons des **[constantes de tests](./assets/constants/tests.py)**, permettant d'activer ou de désactiver un ou plusieurs tests en particulier.

- Deux tests d'intégration globale sont aussi inclus pour valider votre approche, à même les tests unitaires.

## Remise

- Pour soumettre votre travail, créez un fichier zip nommé `LXX-YY-TP2.zip`, où `XX` est le numéro de votre section de laboratoire et `YY` le numéro de votre équipe (par exemple, `L02-04-TP2.zip` pour la section 02, équipe 04).

- Incluez uniquement, dans ce zip, votre script **`exercice.py`** et votre fichier répondu **`boni.txt`** si vous souhaitez courir la chance de remporter un point boni.

- Cela dit, assurez-vous que chaque script fonctionne correctement et déposez le fichier zip dans la boîte Moodle du TP correspondant à votre section. Aussi, assurez-vous d'exécuter le fichier `test-exercice.py` pour valider vos solutions avant de soumettre le fichier zip.

## Barème

| Fonctions                            | Points |
| ------------------------------------ | ------ |
| ajouter_caracteres_dico              | 2      |
| ajouter_codes_morts_dico             | 2      |
| ajouter_fonctions_asm_dico           | 2      |
| ajouter_autres_symboles_dico         | 2      |
| creer_dictionnaire                   | 1      |
| calculer_longueur_clefs_dictionnaire | 2      |
| transpiler                           | 3      |
| transpilation                        | 1      |
| obfusquer_contenu                    | 3      |
| inverser_dictionnaire                | 1      |
| obfuscation                          | 1      |
| Bonus                                | 1      |
| **Total**                            | **20** |
