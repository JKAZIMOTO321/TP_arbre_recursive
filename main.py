"""
Groupe Numero 4
les participants sont :

1. MUMBERE KAZIMOTO JOSUE 4630
2. KASEREKA KAVUGHE SAMY 4614
3. VIHUNDIRA ASIFIWE 4628
4. KATSUVA ELIAS 4617
"""
table_matiere = {
    "Chapitre 1": {
        "Section 1.1": {},
        "Section 1.2": {
            "Sous-section 1.2.1": {},
            "Sous-section 1.2.2": {}
        }
    },
    "Chapitre 2": {
        "Section 2.1": {},
        "Section 2.2": {}
    }
}

def afficher_preordre(arbre, niveau=0):
    for titre, enfants in arbre.items():
        print("  " * niveau + "|-- " + titre)
        afficher_preordre(enfants, niveau + 1)

def compter_noeuds(arbre):
    total = 0
    for enfants in arbre.values():
        total += 1  # Compter le noeud courant
        total += compter_noeuds(enfants)
          # Compter les noeuds enfants
    return total

def ajouter_element(arbre, cible, nouveau):
    for titre, enfants in arbre.items():
        if titre == cible:
            enfants[nouveau] = {}
            print(f"'{nouveau}' ajouté sous '{cible}'.")
            return True
        
        if ajouter_element(enfants, cible, nouveau):
            return True

    return False

def rechercher(arbre, cible, chemin=""):
    for titre, enfants in arbre.items():
        if titre == cible:
            return chemin + "/" + titre

        resultat = rechercher(enfants, cible, chemin + "/" + titre)
        if resultat:
            return resultat

    return None

# creation du menu interactif pour l'utilisateur
def menu():
    while True:
        print("\n======================")
        print("  MENU TABLE DES MATIÈRES")
        print("======================")
        print("1. Afficher la table des matières")
        print("2. Ajouter un élément")
        print("3. Compter les éléments")
        print("4. Rechercher un élément")
        print("5. Quitter")

        choix = input("\nVotre choix : ")

        match choix:
            case "1":
                print("\n--- AFFICHAGE DE LA TABLE ---")
                afficher_preordre(table_matiere)

            case "2":
                cible = input("Ajouter dans quel chapitre/section ? ")
                nouveau = input("Nom de la nouvelle section : ")
                if not ajouter_element(table_matiere, cible, nouveau):
                    print("Élément cible introuvable.")

            case "3":
                total = compter_noeuds(table_matiere)
                print(f"Nombre total d'éléments : {total}")

            case "4":
                cible = input("Nom de l’élément à rechercher : ")
                resultat = rechercher(table_matiere, cible)
                if resultat:
                    print("Trouvé :", resultat)
                else:
                    print("Élément non trouvé.")

            case "5":
                print("Au revoir !")
                break

            case _:
                print("Choix invalide, réessayez.")

menu()