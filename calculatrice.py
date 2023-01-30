from tkinter import *

expression = ""

def appuyer(touche):
    if touche == "=":
        calculer()
        return 

    global expression
    expression += str(touche)
    equation.set(expression)

def calculer():
    try:
        global expression
        total = (eval(expression))

        equation.set(total)
        expression = total
    except:
        equation.set("erreur")
        expression=""

def effacer():
    global expression
    expression = ""
    equation.set("")




if __name__ == "__main__":
    cal = Tk()

    # Couleur
    cal.configure(background="#8C7284")

    # Titre appli
    cal.title("Calculatrice")

    # Taille
    cal.geometry("400x600")

    # Variable pour stocker le contenu actuel
    equation = StringVar()

    # Boite de resultats
    resultat = Label(cal, bg="#9B9FB5", fg="#FFF", textvariable=equation, height=4, width=42)
    resultat.grid(columnspan=4)

    # Boutons
    boutons = [7, 8, 9, "*", 4, 5, 6, "-", 1, 2, 3, "+", 0, ".", "/", "="]
    ligne = 1
    colonne = 0

    for bouton in boutons:
        b = Label(cal, text=str(bouton), bg="#694873", fg="#FFF", height=7, width=10)
        # Rendre le texte cliquable
        b.bind("<Button-1>", lambda e, bouton=bouton: appuyer(bouton))

        # Positionner élément
        b.grid(row=ligne, column=colonne)

        colonne += 1
        if colonne == 4:
            colonne = 0
            ligne += 1


    b = Label(cal, text="Effacer", bg="#e56399", fg="#FFF", height=4, width=42)
    b.bind("<Button-1>", lambda e: effacer())
    b.grid(columnspan=4)
    # Lancer la fenetre
    cal.mainloop()