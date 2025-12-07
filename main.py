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
            return True  # insertion réussie

        # sinon on continue à chercher dans les sous-niveaux
        if ajouter_element(enfants, cible, nouveau):
            return True

    return False  # cible non trouvée


afficher_preordre(table_matiere)
nombre = compter_noeuds(table_matiere)
print(f"\nNombre total de sections et sous-sections : {nombre}")