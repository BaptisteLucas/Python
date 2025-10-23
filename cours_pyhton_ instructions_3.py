
Saisie_notes = [12 , 14.5 , 13 , 17.5]

for Note in Saisie_notes:
    print(Note)


Plateformes = ["Facebook", "Instagram", "Snapchat", "Twitter"]

for Plateforme in Plateformes:
    print(Plateforme)


Mon_nom = "Lucas"

for Epelle in Mon_nom:
    print(Epelle)

Mon_dico = {
"Professeur":"Lucas" , 
"Sympa":True , 
"Matiere_1":"Electronique" , 
"Matiere_2":"Python"
}

for Cle in Mon_dico:
    print(Cle)


for Valeur in Mon_dico.values():
    print(Valeur)

for Cle, Valeur in Mon_dico.items():
    print(f"{Cle} : {Valeur}")

