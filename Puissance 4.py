import json
import math, time
import tkinter as tk
from random import randint

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
    for l in range(LIGNES - 3):
      if grille[l][c] == jeton and grille[l + 1][c] == jeton and grille[l + 2][c] == jeton and grille[l + 3][c] == jeton:
        return True
      
  #vérifie les diagonales qui monte vert la droite
  for c in range(COLONNES - 3):
    for l in range(LIGNES - 3):
      if grille[l][c] == jeton and grille[l + 1][c + 1] == jeton and grille[l + 2][c + 2] == jeton and grille[l + 3][c + 3] == jeton:
        return True

#vérifie les diagonales qui monte vert la gauche
  for c in range(COLONNES - 3):
    for l in range(2, LIGNES):
      if grille[l][c] == jeton and grille[l - 1][c + 1] == jeton and grille[l - 2][c + 2] == jeton and grille[l - 3][c + 3] == jeton:
        return True

def grille_pleine(grille):
  for l in range(LIGNES):
    for c in range(COLONNES):
      if grille[l][c] == 0:
        return False
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
    self.historique = []

#---Scores---
    self.scorej1 = 0
    self.scorej2 = 0
    self.label_score = tk.Label(fenetre, text="J1: 0   J2: 0", font=("Arial", 16), bg="dark blue", fg="white")
    self.label_score.pack(pady=10)
    
#---Bouttons---
    self.canvas = tk.Canvas(fenetre, width=COLONNES*TAILLE, height=LIGNES*TAILLE, bg="dark blue")
    self.canvas.pack()
    self.canvas.create_text((COLONNES * TAILLE)//2, (LIGNES * TAILLE)//2, font=("Arial", 40), text="Puissance 4 =)", fill="White")

    self.bouton_annuler = tk.Button(fenetre, text="<Annuler<", command=self.retour, bg="orange")
    self.bouton_annuler.pack_forget()

    self.bouton_nouvelleParti = tk.Button(fenetre, text="Nouvelle Partie", command=self.commencer, bg="green")
    self.bouton_nouvelleParti.pack(side=tk.LEFT, padx=10)
    
    self.bouton_sauvegarder = tk.Button(fenetre, text="Sauvegarder", command=self.sauvegarder_partie, bg="light blue")
    self.bouton_sauvegarder.pack_forget()
    
    self.bouton_charger = tk.Button(fenetre, text="Charger", command=self.charger_partie, bg="yellow")
    self.bouton_charger.pack(side=tk.LEFT, padx=10)

  def commencer(self):
    self.canvas.bind("<Button-1>", self.clic)
    self.bouton_sauvegarder.pack(side=tk.LEFT, padx=10)
    self.bouton_annuler.pack(side=tk.LEFT, padx=10)
    self.bouton_nouvelleParti.pack_forget()

    self.grille = nv_grille()
    self.joueur = randint(1, 2)
    self.Emplacements()
    self.bouton_annuler.config(state="normal")

  def sauvegarde_etat(self):
    copie = [row[:] for row in self.grille]
    self.historique.append(copie)

  def sauvegarder_partie(self):
    data = {"grille": self.grille, "joueur": self.joueur, "historique": self.historique, "scorej1": self.scorej1, "scorej2": self.scorej2}
    with open('sauvegarde_p4.json', 'w') as f:
      json.dump(data, f)

    print("partie sauvegardée.")

  def charger_partie(self):
    try:
      with open('sauvegarde_p4.json', 'r') as f:
        data = json.load(f)
    except FileNotFoundError:
      print("Aucune sauvegarde trouvée.")
      return
    
    self.grille = data["grille"]
    self.joueur = data["joueur"]
    self.historique = data["historique"]
    self.scorej1 = data["scorej1"]
    self.scorej2 = data["scorej2"]
    self.maj_score()

    self.canvas.bind("<Button-1>", self.clic)
    self.bouton_annuler.pack(side=tk.LEFT, padx=10)
    self.bouton_annuler.config(state="normal")

    self.Emplacements()
    self.fenetre.title(f"Puissance4 - Tour - Joueur{self.joueur}")
    print("Partie chargée.")

  def maj_score(self):
    self.label_score.config(text=f"J1: {self.scorej1} J2: {self.scorej2}")

  def retour(self):
    if not self.historique:
      return
    self.grille = self.historique.pop()
    self.joueur = 2 if self.joueur == 1 else 1
    self.Emplacements()
    self.fenetre.title(f"Puissance4 - Tour - Joueur{self.joueur}")
  
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
    
    self.sauvegarde_etat()
    self.grille[ligne][col] = self.joueur
    self.Emplacements()

    if lg_gagnant(self.grille, self.joueur):
      if self.joueur == 1:
        self.scorej1 += 1
      else:
        self.scorej2 += 1

      self.maj_score()
      self.canvas.unbind("<Button-1>")
      self.bouton_annuler.config(state="disabled")
      self.canvas.create_text((COLONNES * TAILLE)//2, (LIGNES * TAILLE)//2, text=f"Joueur{self.joueur} à Gagné !", fill="red" if self.joueur == 1 else "yellow" , font=("Arial", 32, "bold"))
      self.fenetre.title("Puissance4 - Partie Terminer")
      self.bouton_nouvelleParti.pack(side=tk.LEFT, padx=10)
      return
    
    if grille_pleine(self.grille):
      self.canvas.unbind("<Button-1>")
      self.bouton_annuler.config(state="disabled")
      self.canvas.create_text((COLONNES * TAILLE)//2, (LIGNES * TAILLE)//2, text="Partie Nul !", fill="White" , font=("Arial", 32, "bold"))
      self.fenetre.title("Puissance4 - Partie Nul")
      self.bouton_nouvelleParti.pack(side=tk.LEFT, padx=10)

    self.joueur = 2 if self.joueur == 1 else 1
    self.fenetre.title(f"Puissance4 - Tour - Joueur{self.joueur}")

fenetre = tk.Tk()
Puissance4(fenetre)
fenetre.mainloop()
