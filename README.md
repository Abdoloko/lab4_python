📚 TP Python – Polymorphisme et Exceptions
Objectifs pédagogiques

Explorer le polymorphisme et le duck typing.

Créer des classes abstraites et sous-classes.

Implémenter des exceptions personnalisées pour gérer les erreurs métier.

Structurer un projet Python clair et testable.

Écrire des tests unitaires pour valider le comportement des classes et fonctions.

🗂 Structure générale du projet
TP_Python/
│
├── src/
│   ├── animal.py          # Exercice 1 : polymorphisme Animal
│   ├── compte.py          # Exercice 1 bis : exceptions CompteBancaire
│   ├── forme.py           # Exercice 2 : polymorphisme Forme
│   ├── paiement.py        # Exercice 2 bis : polymorphisme Paiement
│   ├── reservation.py     # Exercice 2 : exceptions Evenement
│   ├── csv_reader.py      # Exercice 3 : import CSV sécurisé
│   └── main.py            # Points d’entrée
│
├── tests/
│   ├── test_animal.py
│   ├── test_compte.py
│   ├── test_forme.py
│   ├── test_paiement.py
│   ├── test_reservation.py
│   └── test_csv.py
│
├── data/                  # CSV d’exemple
│   └── articles.csv
│
├── requirements.txt       # pytest
└── README.md

⚙️ Instructions VS Code

Ouvrir le projet dans VS Code.

Créer un environnement virtuel :

python -m venv .venv


Activer l’environnement :

Windows : .venv\Scripts\activate

macOS/Linux : source .venv/bin/activate

Installer les dépendances :

pip install -r requirements.txt


Lancer un script principal :

python src/main.py


Exécuter tous les tests unitaires :

pytest

📖 Exercices
Exercice 1 – Polymorphisme Animal

Classes : Animal, Chien, Chat, (extension : Vache, Robot)

Méthode commune : parler()

Objectif : montrer le polymorphisme pur et le duck typing.

Exercice 2 – Formes et Paiements

Formes : Forme (ABC), Cercle, Rectangle, Triangle

Méthode aire() polymorphe

__str__() pour affichage lisible

Paiements : Paiement (ABC), CarteBancaire, PayPal, Crypto

Méthode payer() polymorphe

Démonstration du pattern Strategy

Exercice 2 bis – Compte Bancaire et Exceptions

Exceptions personnalisées : SoldeInsuffisantException, MontantNegatifException

Gestion d’erreurs sur les méthodes deposer() et retirer()

Tests unitaires pour valider les comportements

Exercice 2 ter – Réservation d’Événements

Exceptions personnalisées : ReservationException, CapaciteDepasseeException, NomClientInvalideException, NombreInvalideException

Méthode reserver() avec validations

Logger facultatif pour les erreurs

Exercice 3 – Import CSV sécurisé

Exceptions personnalisées : CsvException, FichierIntrouvableException, LigneInvalideException, PrixNegatifException

Fonction charger_csv(chemin) pour retourner une liste de dictionnaires

Gestion des fichiers inexistants, lignes mal formées, prix négatifs
