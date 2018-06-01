#! usr/bin/python
#coding: utf-8
import sys
from Flotte import *
from Bateau import *
import os



def demanderCoord():
	#resultat : retourne la coordonnée saisie par l'utilisateur
	coord=input("") # demande un entier a l'utilisateur
	while coord<0|coord>20: # tant que la coordonee saisie n'est pas dans la grille de jeu
		print("Erreur la coordonnée doit être comprise entre 0 et 20. Recommencez \n")
		coord=input("") # on redemande la saisie
	return coord

def saisieFlotte():
	#resultat : la flotte de 5 bateaux saisie et cree
	flotte=Flotte() #cree une flotte vide
	flotte.ajoutBateau(saisieBateau(1))#ajoute le premier bateau de taille 1

	bat2=saisieBateau(2) # cree un bateau de taille de 2
	while flotte.verifSuperpose(bat2):#tant que le bateau est superpose avec un autre on recommence sa saisie
		print("Le bateau saisi est superposé à un autre. Recommencez la saisie \n ")
		bat2=saisieBateau(2)

	flotte.ajoutBateau(bat2)

	bat3=saisieBateau(3)
	while flotte.verifSuperpose(bat3):
		bat1=saisieBateau(3)

	flotte.ajoutBateau(bat3)

	bat4=saisieBateau(3)
	while flotte.verifSuperpose(bat4):
		bat1=saisieBateau(3)

	flotte.ajoutBateau(bat4)

	bat5=saisieBateau(4)
	while flotte.verifSuperpose(bat5):
		bat5=saisieBateau(4)

	flotte.ajoutBateau(bat5)

	return flotte # retourne la flotte cree avec les bateaux saisis

def saisieBateau(n):

	print("Saisissez les coordonnées d'origine (les coordonnées minimum dans la grille de jeu) du bateau de taille "+str(n)+"\n")
	print("X:\n")
	origineX=demanderCoord()
	print("Y:\n")
	origineY=demanderCoord()

	print("Saisissez l'orientation voulue du bateau dans la grille de jeu (abcisse : x, ordonnée : y)\n")
	orientation=raw_input("") # saisie de l'orientation voulue au clavier

	bateau = Bateau(origineX,origineY,orientation,n) #creation du bateau

	return bateau


def main():
	print("Bienvenue dans notre jeu de bataille navale. Vous vous apprêtez à vivre une expérience unique. Pour commencer saisissez la flotte du joueur 1 \n")
	flotte1=saisieFlotte() #saisie de la flotte du joueur 1
	os.system('clear')
	print("Maintenant saisissez la flotte du joueur 2\n ")
	flotte2=saisieFlotte() #saisie de la flotte du joueur 2
	os.system('clear')
	i=1 #le joueur 1 commence
	flotte=flotte1
	while not(flotte1.couleF() or flotte2.couleF()):
		print("Joueur "+str(i)+", a vous de jouer !")#tant qu'aucune des deux flottes n'est coulee le jeu continue

		if i==1: #si le joueur 1 joue
			flotte1=flotte #la flotte visee au tour d'avant est la flotte 1
			flotte=flotte2 #il vise la flotte 2
			i=2 #le joueur 2 jouera au prochain tour
		else: #si le joueur 2 joue
			flotte2=flotte #la flotte visee au tour d'avant est la flotte 2
			flotte = flotte1 #il vise la flotte 1
		 	i=1 #le joueur 1 jouera au prochain tour

		print("Entrez l'abcisse du tir que vous souhaitez effectuer (entre 0 et 20)\n")
		x=demanderCoord() #saisie de l'abcisse de tir
		print("Entrez l'ordonnée du tir que vous souhaitez effectuer (entre 0 et 20)\n")
		y=demanderCoord() #saisie de l'odonnee de tir



		if flotte.toucheFlotte(x,y):
			#si un des bateaux de la flotte visee est touche
			j=0
			trouve =False
			while j<len(flotte.getBateaux()) and not(trouve):
				if flotte.getBateaux()[j].estOccupee(x,y):
					flotte.getBateaux()[j].touche(x,y)
					trouve= True
					print("touche ")
					if flotte.getBateaux()[j].couleB():
						print("coule\n")
				j=j+1

		elif flotte.enVueF(x,y):
			#si aucun des bateaux n'est touche et l'un d'eux est en vue
			print("En vue \n")
		else:
			print("A l'eau\n")

	print("Game Over ! Le joueur "+str(i)+" a perdu !")
	return -1

main()

############################  MODIFICATIONS DYE_RIVIERE ############################

### les sus.argv[] pnt été remplacés par des input / raw_input
### LE MAIN N'APPLIQUE PAS LES DEGATS SUR LE BATEAU TOUCHE. IL RENVOIE JUSTE SI UN BATEAU DE LA FLOTTE EST TOUCHE PAR LE COUPLE DE COORDONNEES RENTREES.
