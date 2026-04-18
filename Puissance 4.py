import math, time

#1/
#Création d'une Grille 6 par 7

LIGNES = 6
COLOGNES = 7

def afficher(grille):
    for l in grille[::-1]:
        print(" ".join(str(l)))

def nv_grille():
  return [[0 for _ in range(COLOGNES)] for _ in range(LIGNES)]

def placer(grille, cl, lg, jeton):
  grille[lg][cl] = jeton

def position_vd(grille, cl):
  return grille[LIGNES - 1][cl] == 0

def prochaine_ligne(grille, cl):
  for l in range(LIGNES):
    if grille[l][cl] == 0:
      return int(l)

def lg_gagnant(grille, jeton):

  #vérifie les horizontales
  for c in range(COLOGNES - 3):
    for l in range(LIGNES):
      if grille[l][c] == jeton and grille[l][c + 1] == jeton and grille[l][c + 2] == jeton and grille[l][c + 3] == jeton:
        return True
      
  #vérifie les verticales
  for c in range(COLOGNES):
    for l in range(LIGNES - 3):
      if grille[l][c] == jeton and grille[l + 1][c] == jeton and grille[l + 2][c] == jeton and grille[l + 3][c] == jeton:
        return True
      
  #vérifie les diagonales qui monte vert la droite
  for c in range(COLOGNES - 3):
    for l in range(LIGNES - 3):
      if grille[l][c] == jeton and grille[l + 1][c + 1] == jeton and grille[l + 2][c + 2] == jeton and grille[l + 3][c + 3] == jeton:
        return True

#vérifie les diagonales qui monte vert la gauche
  for c in range(COLOGNES - 3):
    for l in range(3, LIGNES):
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
print("! PARTIE TERMINER !")

#!! CE QU'IL RESTE A FAIRE!!
#Essayer de crée une interface pour le jeu
