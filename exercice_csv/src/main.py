from csv_reader import charger_csv, FichierIntrouvableException, LigneInvalideException, PrixNegatifException

if __name__ == "__main__":
    chemin = "data/articles.csv"

    try:
        articles = charger_csv(chemin)
        print("Articles chargés avec succès :")
        for art in articles:
            print(f"{art['id']} - {art['nom']} : {art['prix']}€")
    except FichierIntrouvableException as e:
        print("Erreur :", e)
    except LigneInvalideException as e:
        print("Erreur :", e)
    except PrixNegatifException as e:
        print("Erreur :", e)
