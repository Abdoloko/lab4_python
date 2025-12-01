from compte import CompteBancaire, SoldeInsuffisantException

if __name__ == "__main__":
    try:
        compte = CompteBancaire("Alice", 100)
        compte.afficher()

     
        compte.retirer(150)
    except SoldeInsuffisantException as e:
        print("Erreur:", e)


    compte.deposer(50)
    compte.afficher()

    compte.retirer(70)
    compte.afficher()
