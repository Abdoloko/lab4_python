
class SoldeInsuffisantException(Exception):
    def __init__(self, message):
        super().__init__(message)

class MontantNegatifException(Exception):
    def __init__(self, message):
        super().__init__(message)


class CompteBancaire:
    def __init__(self, nom, solde=0):
        self.nom = nom
        self.solde = solde

    def deposer(self, montant):
        if montant < 0:
            raise MontantNegatifException("Le montant du dépôt doit être positif.")
        self.solde += montant

    def retirer(self, montant):
        if montant > self.solde:
            raise SoldeInsuffisantException("Solde insuffisant pour ce retrait.")
        if montant < 0:
            raise MontantNegatifException("Le montant du retrait doit être positif.")
        self.solde -= montant

    def afficher(self):
        print(f"Compte: {self.nom}, Solde: {self.solde}€")
