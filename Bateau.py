#-*- coding: utf-8 -*-
class Bateau:
	def __init__(self,origineX,origineY,orientation, taille):
		#creerBateau: int*int*str*int => bateau
		#donnee: origineX et origineY les coordonnees d'origine du bateau sur la grille (coordonnees les plus basses du bateau)
		#orientation : char "x" si l'orientation est selon les abcisses, "y" selon les ordonnees, taille entier taille du bateau
		#resultat : objet de type bateau, erreur si le bateau n'appartient pas a la grille
		#pre: origineX et origineY comprises entre 0 20, orientation = x ou =y, taille comprise en 1 et 4 INCLUS
		self.tabCords=[]
		if((origineX<0) or (origineY<0)):
			raise Exception("L'une des origines est negative")
		elif((origineX>20) or (origineY>20)):
			raise Exception("L'une des coord est plus grande que 20")
		elif((orientation=="x") and (origineX+taille-1>20)):
			raise Exception("Le bateau sort de la grille")
		elif((orientation=="y") and (origineY+taille-1>20)):
			raise Exception("Le bateau sort de la grille")
		elif(not((orientation=="x") or (orientation =="y"))):
			raise Exception("L orientation est incorrecte")
		elif((taille<1) or (taille>4)):
			raise Exception("La taille du bateau non comprise entre 1 et 4")
		else:
			tabCord=[]
			if(orientation=="x"):
				for i in range(0,taille):
					tabCord.append((origineX,origineY+i))
			else:
				for j in range(0,taille):
					tabCord.append((origineX+j,origineY))
			self.tabCords = tabCord

	def taille(self): #bateau => int
		#donnee: un bateau initialisé non vide
		#resultat: le nombre de cases occupees par le bateau
		if(self.tabCords==[]):
			raise Exception("Bateau non initialisé")
		else:
			return len(self.tabCords)

	def touche(self,x,y):#bateau*int*int => bateau
		#donnee: bateau et deux entiers (coordonnees sur lequelles le bateau se situe )
		#resultat: retourne le bateau mais il n'occupe plus la case touchee, retourne erreur si x et y ne correspondent pas à des coordonees du bateau
		#pre : bateau avec taille comprise entre 1 et 4 et coordonnees comprises entre 0 et 20
		if(self.tabCords==[]):
			raise Exception("Bateau non initialisé")
		elif(not(self.estOccupee(x,y))):
			raise Exception("La case n'est pas occupée donc ne peut etre touchée")
		else:
			trouve=False
			i=0
			while((not(trouve)) and (i<self.taille())):
				if(self.tabCords[i]==(x,y)):
					trouve=True
					self.tabCords[i]=(-1,-1)
				i= i+1
		return self


	def estOccupee(self,x,y):#bateau*int*int => bool
		#donnee: un objet de type bateau et deux entiers correspondant à des coordonnees de la grille
		#resultat : true si les coordonnes correspondent a une case du bateau, false sinon. Une case n'est plus occupee si elle a deja ete touchee
		#pre : bateau avec taille comprise entre 1 et 4 et coordonnees comprises entre 0 et 20, SELF UN BATEAU BIEN INITIALISE
		if(self.tabCords==[]):
			raise Exception("Bateau non initialisé")
		elif((x<0) or (y<0)):
			raise Exception("L'une des coordonnees est negative")
		elif((x>20) or (y>20)):
			raise Exception("L'une des coordonnees est plus grande que 20")
		else:
			trouve=False
			i=0
			while((not(trouve)) and (i<self.taille())):
				if(self.tabCords[i]==(x,y)):
					trouve=True
				i= i+1
		return trouve



	def couleB(self):#bateau => bool
		#donnee: objet de type bateau
		#resultat: true si toutes les cases du bateau sont touchees
		#pre : bateau avec taille comprise entre 1 et 4
		if(self.tabCords==[]):
			raise Exception("Bateau non initialisé")
		else:
			coule=True
			i=0
			while(coule and (i<self.taille())):
				coule=coule and (self.tabCords[i]==(-1,-1))
				i=i+1
		return coule

	def enVueB(self,x,y):# bateau*int*int => bool
		#donnee: objet de type bateau et deux entiers correspondant aux coordonnees visees par le joueur adverse
		#resultat: true si le bateau est sur la ligne visee (une des abcisses du bateau = x ) ou sur la colonne visee (une des ordonnees du bateau = y) et que le bateau n'est pas touche, false sinon
		#pre : bateau avec taille comprise entre 1 et 4 et coordonnees comprises entre 0 et 20

		if(self.tabCords==[]):
			raise Exception("Bateau non initialisé")
		elif((x<0) or (y<0)):
			raise Exception("L'une des coordonnee est negative")
		elif((x>20) or (y>20)):
			raise Exception("L'une des coordonnee est plus grande que 20")
		elif(self.estOccupee(x,y)):
			return False
		else:
			enVue=False
			i=0
			while((not(enVue)) and (i<self.taille())):
				if((self.tabCords[i][0]==x) or (self.tabCords[i][1]==y)) :
					enVue=True
				i= i+1
		return enVue

	def getTabCords(self):
		if(self.tabCords==[]):
			raise Exception("Bateau non initialisé")
		return self.tabCords


