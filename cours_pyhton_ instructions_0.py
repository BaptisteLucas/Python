Faim = False
Sommeil = False

def Manger():
    #fonction manger
    global Faim, Sommeil
    Faim = False
    Sommeil = True

def Dormir():
    #fonction dormir
    global Faim, Sommeil
    Sommeil = False
    Faim = True
    
if Faim:
    Manger()
else:
    Dormir()


