from random import randint
import tkinter as tk
from tkinter import messagebox

# Classe pour dessiner UNE fleur 
class Fleur:
    def __init__(self,surface_dessin, x,y):
        self.x = x
        self.y = y
        self.surface_dessin = surface_dessin
        self.quandOnMefface = None 
        self.dessiner()
        self.temp = None
    
    def dessiner(self):
        x = self.x
        xd = x+90
        y = self.y
        yd = y+90
        self.ovals = list()
        self.ovals.append(self.surface_dessin.create_oval(x-40,y-40,xd-55,yd-55,fill='pink'))
        self.ovals.append(self.surface_dessin.create_oval(x-55,y+33,xd-70,yd+18,fill='pink'))
        self.ovals.append(self.surface_dessin.create_oval(x+11,y+70,xd-4,yd+55,fill='pink'))
        self.ovals.append(self.surface_dessin.create_oval(x+70,y+23,xd+55,yd+8,fill='pink'))
        self.ovals.append(self.surface_dessin.create_oval(x+36,y-45,xd+21,yd-60,fill='pink'))
        # Centre de la Fleur
        self.ovals.append(self.surface_dessin.create_oval(x,y,xd,yd,fill='yellow'))

        # Tout effacer quand on clique sur on oval
        for oval in self.ovals:
            self.surface_dessin.tag_bind(oval, '<Button-1>', self.effacer)

    def effacer(self, event): 
        for oval in self.ovals:
            self.surface_dessin.delete(oval)

        if (self.quandOnMefface is not None):
            self.quandOnMefface()

# Classe qui va gerer la creation et destruction DES fleurs
class Peintre:
    def __init__(self):
        # Creer le canvas 
        self.hauteur = 1000
        self.largeur = 1000
        self.compteur = -1
        self.surface_dessin = tk.Canvas(mon_app, width = self.largeur, height = self.hauteur, bg = 'white')
        self.surface_dessin.pack(padx = 5, pady = 5)
        self.surface_dessin.create_text(500, 30, text = "Essayez de faire disparaître la fleur en la cliquant dessus ! ^^", fill="purple", font=('Helvetica 15 bold'))
        self.text1 = self.surface_dessin.create_text(176,960,text = "Regardez combien de tentatives vous avez effectué ",fill="light sea green",font=('Helvetica 10 bold'))
        self.text2 = self.surface_dessin.create_text(170,980,text = "Compteur : 0",font=('Helvetica 9 bold'))
        # Dessiner unen fleur 
        self.dessinerFleur()

    def dessinerFleur(self):
        self.compteur += 1
        x = randint(70, 850)
        y = randint(70, 800)
        self.fleur = Fleur(self.surface_dessin, x, y)
        # Quand on efface une fleur, on en redessine unen autre 
        self.fleur.quandOnMefface = self.dessinerFleur
        monTexte = "Compteur : {valeur}".format(valeur = self.compteur)
        self.surface_dessin.itemconfig(self.text2, text=monTexte)
        # Texte
        self.surface_dessin.pack()

# Fenêtre principale 
mon_app = tk.Tk()
mon_app.title('Flowers')
# Le peintre 
peintre = Peintre()

# Button (bouton Quitter)
Bt1 = tk.Button(mon_app, text = 'Quitter', command = mon_app.destroy).pack(side = tk.RIGHT,padx = 5,pady = 5)

mon_app.mainloop()
