import math, time
import tkinter as tk

#1/
#Création d'une Grille 6 par 7

LIGNES = 6
COLONNES = 7
TAILLE = 80

def afficher(grille):
    for l in grille[::-1]:
        print(" ".join(str(l)))

def nv_grille():
  return [[0 for _ in range(COLONNES)] for _ in range(LIGNES)]

def placer(grille, cl, lg, jeton):
  grille[lg][cl] = jeton

def position_vd(grille, cl):
  return grille[LIGNES - 1][cl] == 0

def prochaine_ligne(grille, cl):
  for l in range(LIGNES):
    if grille[l][cl] == 0:
      return int(l)
  return None

def lg_gagnant(grille, jeton):

  #vérifie les horizontales
  for c in range(COLONNES - 3):
    for l in range(LIGNES):
      if grille[l][c] == jeton and grille[l][c + 1] == jeton and grille[l][c + 2] == jeton and grille[l][c + 3] == jeton:
        return True
      
  #vérifie les verticales
  for c in range(COLONNES):
    for l in range(LIGNES - 2):
      if grille[l][c] == jeton and grille[l + 1][c] == jeton and grille[l + 2][c] == jeton and grille[l + 3][c] == jeton:
        return True
      
  #vérifie les diagonales qui monte vert la droite
  for c in range(COLONNES - 3):
    for l in range(LIGNES - 2):
      if grille[l][c] == jeton and grille[l + 1][c + 1] == jeton and grille[l + 2][c + 2] == jeton and grille[l + 3][c + 3] == jeton:
        return True

#vérifie les diagonales qui monte vert la gauche
  for c in range(COLONNES - 3):
    for l in range(2, LIGNES):
      if grille[l][c] == jeton and grille[l - 1][c + 1] == jeton and grille[l - 2][c + 2] == jeton and grille[l - 3][c + 3] == jeton:
        return True

def ErreurVal(cl):

#Vérifie que l'input est correct
  try:
      cl = int(input("!! Une valeur incorrect à était rentrer, réessayer !!, colonne(1 à 7): ")) - 1
      return cl
  except ValueError:
    ErreurVal(cl)
  if cl != 0 or 1 or 2 or 3 or 4 or 5 or 6:
    ErreurVal(cl)

grille = nv_grille()
Jeu_Terminer = False
Tour = 0

class Puissance4:
  def __init__(self, fenetre):
    self.fenetre = fenetre
    self.fenetre.title("Puissance4")

    self.grille = nv_grille()
    self.joueur = 1

    self.canvas = tk.Canvas(fenetre, width=COLONNES*TAILLE, height=LIGNES*TAILLE, bg="dark blue")
    self.canvas.pack()

    self.canvas.bind("<Button-1>", self.clic)
    self.Emplacements()

  def Emplacements(self):
    self.canvas.delete("all")

    for l in range(LIGNES):
      for c in range(COLONNES):
        x1 = c * TAILLE
        y1 = (LIGNES - 1 - l) * TAILLE
        x2 = x1 + TAILLE
        y2 = y1 + TAILLE

        couleur = "black"
        if self.grille[l][c] == 1:
          couleur = "red"
        elif self.grille[l][c] == 2:
          couleur = "yellow"

        self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=couleur)

  def clic(self, event):
    col = event.x // TAILLE
    ligne = prochaine_ligne(self.grille, col)

    if ligne is None:
        return #colonne pleine
    
    self.grille[ligne][col] = self.joueur
    self.Emplacements()

    if lg_gagnant(self.grille, self.joueur):
      self.canvas.unbind("<Button-1>")
      self.canvas.create_text((COLONNES * TAILLE)//2, (LIGNES * TAILLE)//2, text=f"Joueur{self.joueur} à Gagné !", fill="red" if self.joueur == 1 else "yellow" , font=("Arial", 32, "bold"))
      self.fenetre.title("Puissance4 - Partie Terminer")
      return
    
    self.joueur = 2 if self.joueur == 1 else 1
    self.fenetre.title(f"Puissance4 - Tour - Joueur{self.joueur}")

fenetre = tk.Tk()
Puissance4(fenetre)
fenetre.mainloop()

"""""
#Test
afficher(grille)

while not Jeu_Terminer:
  if Tour == 0:


    #Tour du Joueur 1

    #Vérifie que ErreurVal() est correct
    try:
      cl = "Input"
      cl = int(input("Tour du Joueur 1, colonne(1 à 7): ")) - 1
    except ValueError:
        cl = ErreurVal(cl)
  

    if position_vd(grille, cl):
      lg = prochaine_ligne(grille, cl)
      placer(grille, cl, lg, 1)

      #Test
      afficher(grille)

      if lg_gagnant(grille, 1) == True:
        print("LE JOUEUR 1 à gagné !")
        Jeu_Terminer = True

      Tour += 1

  #Tour du Joueur 2
  
  else:

     #Vérifie que ErreurVal() est correct
    try:
      cl = "Input"
      cl = int(input("Tour du Joueur 1, colonne(1 à 7): ")) - 1
    except ValueError:
        cl = ErreurVal(cl)

    if position_vd(grille, cl):
      lg = prochaine_ligne(grille, cl)
      placer(grille, cl, lg, 2)
    
    #Test
    afficher(grille)

    if lg_gagnant(grille, 2) == True:
        print("LE JOUEUR 2 à gagné !")
        Jeu_Terminer = True


    Tour += 1
    Tour %= 2
time.sleep(1.5)
print("! PARTIE TERMINER !")"""

#!! CE QU'IL RESTE A FAIRE!!
#Quelque correction
