from reservation import Evenement, ReservationException

if __name__ == "__main__":
    try:
        event = Evenement("Concert", 5)
       
        event.reserver("", 2)
    except ReservationException as e:
        print("Erreur:", e)

   
    try:
        event.reserver("Alice", 3)
        event.afficher()
    except ReservationException as e:
        print("Erreur:", e)

   
    try:
        event.reserver("Bob", 3)
    except ReservationException as e:
        print("Erreur:", e)
