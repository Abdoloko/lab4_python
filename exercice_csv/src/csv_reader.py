import csv
import os

# Exceptions
class CsvException(Exception):
    pass

class FichierIntrouvableException(CsvException):
    pass

class LigneInvalideException(CsvException):
    pass

class PrixNegatifException(CsvException):
    pass


def charger_csv(chemin):
    if not os.path.exists(chemin):
        raise FichierIntrouvableException(f"Fichier non trouvé : {chemin}")

    articles = []
    with open(chemin, newline='', encoding='utf-8') as csvfile:
        lecteur = csv.reader(csvfile, delimiter=';')
        for numero_ligne, ligne in enumerate(lecteur, start=1):
            if not ligne or all(not champ.strip() for champ in ligne):
                continue  
            if len(ligne) != 3:
                raise LigneInvalideException(f"Ligne {numero_ligne} invalide : {ligne}")

            id_, nom, prix_str = ligne
            try:
                prix = float(prix_str)
            except ValueError:
                raise LigneInvalideException(f"Ligne {numero_ligne} : prix non numérique")

            if prix < 0:
                raise PrixNegatifException(f"Ligne {numero_ligne} : prix négatif")

            articles.append({"id": id_.strip(), "nom": nom.strip(), "prix": prix})

    return articles
