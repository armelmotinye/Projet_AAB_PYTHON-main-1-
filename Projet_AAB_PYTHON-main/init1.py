
#from evenement import Evenement
from evenements.evenement_dao import EvenementDAO

"""
    # Création d'un événement
Evenement = EvenementDAO
evenement = Evenement.ajouter_evenement("film", "2024-04-30", "15:00", "30", "100", "boul corbusier salle A")
    
     # Ajout de l'événement
    #EvenementDAO.ajouter_evenement(evenement)
print(evenement)

# Affichage des événements
print("Liste des événements après ajout :")
evenements = EvenementDAO.afficher_evenements()
for event in evenements:
        print(event)
"""
"""
    # Modification de l'événement
Evenement = EvenementDAO
#evenement.nom_event("Updated Event")
event = Evenement.modifier_evenement(1, "cinema", "2024-04-30", "15:00", "30", "100", "boul corbusier salle A")
print(event)
"""
"""
    # Affichage des événements après modification
print("\nListe des événements après modification :")
evenements = EvenementDAO.afficher_evenements()
#for event in evenements:
print(evenements)
"""
    # Suppression de l'événement
#EvenementDAO.supprimer_evenement(evenement.id_event())
annuler = EvenementDAO.supprimer_evenement(1)
    # Affichage des événements après suppression
#print("\nListe des événements après suppression :")
#evenements = EvenementDAO.afficher_evenements()
#for event in evenements:
#print(event)  
    
"""if __name__ == "__main__":
    test_functionality()
"""