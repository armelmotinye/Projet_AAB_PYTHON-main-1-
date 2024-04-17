from utilisateurs.utilisateur_dao import UtilisateurDao
#from evenement import Evenement
from evenements.evenement_dao import EvenementDAO

utilisateur_dao = UtilisateurDao
utilisateur1 = utilisateur_dao.add_utilisateur('Math', 'tresor', '35', 'def@test.com', '12345', 'Admin')
print(utilisateur1)

def test_functionality():
    # Création d'un événement
    evenement = Evenement(id_event=None, nom_event="Test Event", date_event="2024-04-30", heure_event="15:00", prix_event=30.0, nombre_places_event=100, lieu_event="boul corbusier salle A")
    
    print(evenement)