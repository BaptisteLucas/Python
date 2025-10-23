Faim = False
Excite = True
Sommeil = False

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

if Faim:
    Manger()
elif Excite:
    Jouer()
else:
    Dormir()


