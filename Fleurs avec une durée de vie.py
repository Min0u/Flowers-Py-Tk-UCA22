import tkinter as tk

Hauteur = 1000
Largeur = 1000

# Fenêtre principale 
mon_app = tk.Tk()
mon_app.title('Flowers')

# Canvas
surface_dessin = tk.Canvas(mon_app, width = Largeur, height = Hauteur, bg = 'white')
surface_dessin.pack(padx = 5, pady = 5)

tk.messagebox.showinfo("Coucou !", "Cliquer pour faire apparaitre des fleurs :) \nSa durée de vie est de quelques secondes après elle disparaitra :'(")

fleurs = list()

def clic(event):
    # Apparition d'une nouvelle fleur
    x = event.x
    y = event.y
    nvlFleur = Fleur(x,y)
    nvlFleur.dessiner()
    fleurs.append(nvlFleur)

# En cliquant clic s'exécute
surface_dessin.bind('<Button-1>', clic)
surface_dessin.pack(padx =5, pady =5)

class Fleur:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.age = 0
    def dessiner(self):
        x = self.x
        xd = x+90
        y = self.y
        yd = y+90
        self.ovals = list()
        self.ovals.append(surface_dessin.create_oval(x-40,y-40,xd-55,yd-55,fill='pink'))
        self.ovals.append(surface_dessin.create_oval(x-55,y+33,xd-70,yd+18,fill='pink'))
        self.ovals.append(surface_dessin.create_oval(x+11,y+70,xd-4,yd+55,fill='pink'))
        self.ovals.append(surface_dessin.create_oval(x+70,y+23,xd+55,yd+8,fill='pink'))
        self.ovals.append(surface_dessin.create_oval(x+36,y-45,xd+21,yd-60,fill='pink'))
        # Centre de la Fleur
        self.ovals.append(surface_dessin.create_oval(x,y,xd,yd,fill='yellow'))

# Durée de vie
def tictoc():
    for fleur in fleurs:
        fleur.age += 1
        if fleur.age > 10 :
            for oval in fleur.ovals:
                surface_dessin.delete(oval)
    surface_dessin.after(100,tictoc)
    
# Button (bouton Quitter)
Bt1 = tk.Button(mon_app, text = 'Quitter', command = mon_app.destroy).pack(side = tk.RIGHT,padx = 5,pady = 5)

tictoc()
mon_app.mainloop()
