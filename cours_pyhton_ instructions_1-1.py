Faim = False
Excite = True
Sommeil = False
Mon_age_de_chat = 0.0

def Manger():
    #fonction manger
    global Faim, Excite
    Faim = False
    Excite = True

def Jouer():
    #fonction jouer
    global Excite, Sommeil
    Excite = False
    Sommeil = True

def Dormir():
    #fonction dormir
    global Sommeil, Faim
    Sommeil = False
    Faim = True

while Mon_age_de_chat < 15.0:
    if Faim:
        Manger()
    elif Excite:
        Jouer()
    else:
        Dormir()
    Mon_age_de_chat += 1/365
    
print("Le chat a vécu %.2f ans, soit %.2f ans en âge humain!" 
      % (Mon_age_de_chat, Mon_age_de_chat * 7))
