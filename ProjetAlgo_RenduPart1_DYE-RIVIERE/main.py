#coding:utf8
from typeAbstrait import *
def positionner_bateau (taille):
	x=-1
	y=-1
	orient='a'
	while ((x<0) or (x>20)):
		x= input("Choisisez l'abscisse de la premiere case du bateau: x=")
	while ((y<0) or (y>20)):
		y= input("Choisisez l'ordonnée de la premiere case du bateau: y=")
	while (not((orient=='h') or (orient=='v'))):
		orient= raw_input("Son orientation (h pour horizontal, v pour vertical) :")
	if((orient=='h') and ((x+taille)<21)):
		tabCord=[]
		for i in range(0,(taille+1)):
			tabCord.append((x+i,y))
		return creer_bateau(tabCord)
	elif((orient=='v') and ((y+taille)<21)):
		tabCord2=[]
		for i in range(0,(taille+1)):
			tabCord2.append((x,y+i))
		return creer_bateau(tabCord2)
	else:
		print("Votre bateau sort de la grille ! Recommencons...")
		return positionner_bateau(taille)

def main():
	print("Rentrer bateau de taille 1 J1 :")
	bat11=positionner_bateau(1)
	print("Rentrer bateau de taille 2 J1 :")
	bat12=positionner_bateau(2)
	print("Rentrer bateau de taille 3 J1 :")
	bat13=positionner_bateau(3)
	print("Rentrer bateau de taille 3 J1 :")
	bat14=positionner_bateau(3)
	print("Rentrer bateau de taille 4 J1 :")
	bat15=positionner_bateau(4)
	print("Rentrer bateau de taille 1 J2 :")
	bat21=positionner_bateau(1)
	print("Rentrer bateau de taille 2 J2 :")
	bat22=positionner_bateau(2)
	print("Rentrer bateau de taille 3 J2 :")
	bat23=positionner_bateau(3)
	print("Rentrer bateau de taille 3 J2 :")
	bat24=positionner_bateau(3)
	print("Rentrer bateau de taille 4 J2 :")
	bat25=positionner_bateau(4)

	tabBat1 = [bat11,bat12,bat13,bat14,bat15]
	tabBat2 = [bat21,bat22,bat23,bat24,bat25]
	
	joueur1=creer_joueur(tabBat1)
	joueur2=creer_joueur(tabBat2)
	
	tabj=[joueur1,joueur2]
	
	p=creer_Partie(tabj)
	
	tour=1 #1 quand c'est le tour du joueur 1, et 2 quand c'est le tour du second
	while(not(fin_partie(p))):
		x = input("\n Joueur "+tour+", à vous de jouer ! Rentrez la première coordonnée x de tir :")
		y = input("\n Rentrez la coordonnée y de tir :")
		
		trouve = False
		envue = False
		
		bat = get_bateaux_joueur(get_joueur_partie(tour-1))

		for i in range(0,6):
			trouve = est_touche(bat[i],x,y)
			if(trouve):
				indexbat = i
			envue = (envue)or(est_en_vue(bat[i],x,y))
		
		if(trouve):
			print("\nTouché")
			appliquer_degats(bat[indexbat],x,y)
			if(est_coule(bat[indexbat])):
				print("\nCoulé")
		elif(envue):
			print("\nEn vue")
		else:
			print("\nA l'eau")
		
		if(tour==1):
			tour=2
		else:
			tour=1

	print("Le joueur "+tour+" a perdu ! ")

main()
