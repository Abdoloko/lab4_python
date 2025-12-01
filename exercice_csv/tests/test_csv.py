import pytest
from src.csv_reader import charger_csv, FichierIntrouvableException, LigneInvalideException, PrixNegatifException
import os

def test_fichier_valide(tmp_path):
 
    fichier = tmp_path / "articles.csv"
    fichier.write_text("1;Article1;10\n2;Article2;20\n3;Article3;30\n")
    result = charger_csv(str(fichier))
    assert len(result) == 3
    assert result[0]["nom"] == "Article1"

def test_fichier_inexistant():
    with pytest.raises(FichierIntrouvableException):
        charger_csv("fichier_inexistant.csv")

def test_prix_non_numerique(tmp_path):
    fichier = tmp_path / "articles.csv"
    fichier.write_text("1;Article1;abc\n")
    with pytest.raises(LigneInvalideException):
        charger_csv(str(fichier))

def test_prix_negatif(tmp_path):
    fichier = tmp_path / "articles.csv"
    fichier.write_text("1;Article1;-5\n")
    with pytest.raises(PrixNegatifException):
        charger_csv(str(fichier))

def test_ligne_invalide(tmp_path):
    fichier = tmp_path / "articles.csv"
    fichier.write_text("1;Article1\n")  # seulement 2 colonnes
    with pytest.raises(LigneInvalideException):
        charger_csv(str(fichier))
