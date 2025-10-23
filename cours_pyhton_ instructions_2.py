Etat = "sommeil"
Mon_age_de_chat = 0.0

def Manger():
    #fonction manger
    global Etat
    Etat = "excité"

def Jouer():
    #fonction jouer
    global Etat
    Etat = "sommeil"

def Dormir():
    #fonction dormir
    global Etat
    Etat = "faim"

while Mon_age_de_chat < 15.0:
    match Etat:
        case "faim":
            Manger()
        case "excité":
            Jouer()
        case "sommeil":
            Dormir()
        case _:
            print("Un chat ne sait rien faire d'autre")
    Mon_age_de_chat += 1/365

print("Le chat a vécu %.2f ans, soit %.2f ans en âge humain!" % (Mon_age_de_chat, Mon_age_de_chat * 7))


