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
        print("  " * niveau + "- " + titre)
        afficher_preordre(enfants, niveau + 1)