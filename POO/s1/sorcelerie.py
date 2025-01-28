import random

# Grimoire magique enrichi
grimoire: list[dict[str, str | bool]] = [
    {"nom": "Mur de Lumière", "type": "Protection", "interdit": False},
    {"nom": "Flammes Infernales", "type": "Destruction", "interdit": True},
    {"nom": "Bouclier de Givre", "type": "Protection", "interdit": False},
    {"nom": "Nova Arcanique", "type": "Destruction", "interdit": False},
    {"nom": "Portail de l'Ombre", "type": "Invocation", "interdit": True},
    {"nom": "Brume de Soins", "type": "Soin", "interdit": False},
    {"nom": "Lance de Foudre", "type": "Destruction", "interdit": False},
    {"nom": "Aura Purifiante", "type": "Protection", "interdit": False},
    {"nom": "Vortex Maudit", "type": "Destruction", "interdit": True},
    {"nom": "Invocation d'Esprit Ancien", "type": "Invocation", "interdit": False},
    {"nom": "Restauration Divine", "type": "Soin", "interdit": False},
    {"nom": "Explosion de Mana", "type": "Destruction", "interdit": False},
]

# Banque de missions
missions: list[dict[str, str | list[str]]] = \
    [
        {
            "description": "Une tempête magique menace la forêt. Vous devez créer un bouclier protecteur.",
            "sorts_requis": ["Protection"],
        },
        {
            "description": "Des créatures maléfiques envahissent la région. Vous devez les éliminer.",
            "sorts_requis": ["Destruction"],
        },
        {
            "description": "Un esprit ancien est en colère. Vous devez invoquer un allié pour l'apaiser.",
            "sorts_requis": ["Invocation"],
        },
        {
            "description": "Un village voisin est frappé par une maladie magique. Vous devez soigner les blessés.",
            "sorts_requis": ["Soin"],
        },
        {
            "description": "Une barrière de feu bloque votre chemin. Vous devez créer un bouclier magique pour traverser.",
            "sorts_requis": ["Protection", "Destruction"],
        },
        {
            "description": "Un golem gigantesque attaque ! Vous devez l'affaiblir et vous protéger.",
            "sorts_requis": ["Destruction", "Protection"],
        },
        {
            "description": "Un portail instable menace d'engloutir la région. Vous devez invoquer une entité protectrice et sceller le portail.",
            "sorts_requis": ["Invocation", "Protection"],
        },
        {
            "description": "Les morts-vivants envahissent la forêt. Vous devez les éliminer et purifier la zone.",
            "sorts_requis": ["Destruction", "Soin"],
        }
    ]
def donner_mission(lst_missions, grimoire):
    """
    Effectue toutes les opérations pour assurer le fonctionnement de la mission
    :param lst_missions: Liste de missions les contenant en forme de dictionnaires.
    :param grimoire: Liste de sorts les contenant en forme de dictionnaires.
    :return: None
    """
    while True:
        mission = random.choice(lst_missions)
        sorts_interdits = input(f"Votre mission: {mission["description"]}\n"
                                f"Utiliser les sorts interdits? (O/N): ").upper()
        num = 1
        match sorts_interdits: # montrer la liste de choix à l'utilisateur
            case "O":
                for sort in grimoire:
                    if sort["interdit"]:
                        print(f"{num}. {sort['nom']} (interdit)") # distinguer les sorts interdits des sorts normaux
                    else:
                        print(f"{num}. {sort['nom']}") # sorts normaux
                    num += 1 # incrémenter pour le prochain nombre dans la liste
            case "N":
                for sort in grimoire:
                    if not sort["interdit"]: # montrer la liste si l'utilisateur décide de ne pas utiliser de sorts interdits
                        print(f"{num}. {sort['nom']}")
                        num += 1
        # choix de l'utilisateur
        choix = input("Choisissez les sorts [ex: 1,4]: ")
        for sort in choix.split(","): # validation de chaque sort utilisé par l'utilisateur
            if grimoire[int(sort)-1]["type"] in mission["sorts_requis"]:
                if grimoire[int(sort) - 1]["interdit"]:
                    num = random.randint(0,1000) # 50% de chance qu'un sort interdit tourne mal
                    if num % 2 == 0:
                        print("BOOM!")
                        break
                    else: # enlever les sorts de la liste de sorts requis s'ils ont le bon type
                        mission["sorts_requis"].remove(grimoire[int(sort)-1]["type"])
                else:
                    mission["sorts_requis"].remove(grimoire[int(sort) - 1]["type"])

        if not mission["sorts_requis"]: # si tous les bons types de sorts ont été bien utilisés
            print("Vous avez vaincu la menace et gagné l'admiration du royaume ! 🤩")
        else: # sinon
            print("Well you can't expect to win em all.. :(")
if __name__ == "__main__":
    donner_mission(missions, grimoire)