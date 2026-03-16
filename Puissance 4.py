import math

#1/

LIGNES = 6
COLONNES = 7

#Inverse la matrice et l'aligne.
def afficher(grille):
    for l in grille[::-1]:
        print(" ".join(str(l)))

#Création d'une Grille 6 par 7
def nv_grille():
  return [[0 for _ in range(COLONNES)] for _ in range(LIGNES)]

#Place le jeton du joueur dans la ligne
def placer(grille, cl, lg, jeton):
  grille[lg][cl] = jeton

#Vérifie si l'emplacement choisi est valide
def position_vd(grille, cl):
  return grille[5][cl] == 0

#Si une colonne posséde déja un jeton, place le prochain au dessus
def prochaine_ligne():
  for i in range(LIGNES):
    if grille[i][cl] == 0:
      return int(i)

#Parametre
grille = nv_grille()
Jeu_Terminer = False
Tour = 0

#Test
afficher(grille)

#2/
#Démarage du jeu
while not Jeu_Terminer:
  if Tour == 0:


    #Tour du Joueur 1
    cl = int(input("Tour du Joueur 1, colonne(1 à 7): "))

    if position_vd(grille, cl):
      lg = prochaine_ligne()
      placer(grille, cl, lg, 1)

      Tour += 1

  #Tour du Joueur 2
  else:
    cl = int(input("Tour du Joueur 2, colonne(1 à 7): "))
    if position_vd(grille, cl):
      lg = prochaine_ligne()
      placer(grille, cl, lg, 2)
    
    #Test
    afficher(grille)

    Tour += 1
    Tour %= 2
