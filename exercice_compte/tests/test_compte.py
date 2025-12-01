import pytest
from src.compte import CompteBancaire, SoldeInsuffisantException, MontantNegatifException

def test_depot_retrait():
    compte = CompteBancaire("Bob", 100)
    compte.deposer(50)
    assert compte.solde == 150

    compte.retirer(30)
    assert compte.solde == 120

def test_retrait_insuffisant():
    compte = CompteBancaire("Charlie", 50)
    with pytest.raises(SoldeInsuffisantException):
        compte.retirer(100)

def test_depot_negatif():
    compte = CompteBancaire("Dave", 0)
    with pytest.raises(MontantNegatifException):
        compte.deposer(-10)

def test_retrait_negatif():
    compte = CompteBancaire("Eve", 100)
    with pytest.raises(MontantNegatifException):
        compte.retirer(-20)
