import pytest
from src.reservation import Evenement, CapaciteDepasseeException, NombreInvalideException, NomClientInvalideException

def test_reservation_valide():
    event = Evenement("Theatre", 10)
    event.reserver("Charlie", 5)
    assert event.places_reservees == 5

def test_nom_client_invalide():
    event = Evenement("Expo", 10)
    with pytest.raises(NomClientInvalideException):
        event.reserver("", 2)

def test_nombre_invalide():
    event = Evenement("Cinema", 10)
    with pytest.raises(NombreInvalideException):
        event.reserver("Alice", 0)

def test_capacite_depassee():
    event = Evenement("Concert", 5)
    event.reserver("Bob", 4)
    with pytest.raises(CapaciteDepasseeException):
        event.reserver("Alice", 2)
