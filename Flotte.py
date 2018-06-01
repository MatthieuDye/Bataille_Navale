#-*- coding: utf-8 -*-

class Flotte:
	#type Flotte qui gère 5 bateaux de taille 1 à 4 avec deux de taille 3 

	def __init__(self): #  => Flotte 
		#resultat : une flotte vide 
		self.tabBats=[]

	def getBateaux(self):
		return self.tabBats

	def couleF(self):# Flotte=> bool	
		#donnee: flotte contenant 5 bateaux 
		#resultat: true si tous les bateaux de la flotte sont coules, false sinon 
		if self.getBateaux()==[]:
			raise Exception("La Flotte est vide")
		else:
			l=len(self.tabBats)
			tousCoules = True
			for i in range(0,l):
				b = self.getBateaux()[i]
				tousCoules=tousCoules & b.couleB()
		return tousCoules

	def verifSuperpose(self,bateau):#Flotte*bateau=>bool
		#donnee: flotte et un bateau 
		#resultat: true si le bateau ne se superpose pas avec un autre bateau de la flotte (ses coordonnees ne sont egales a aucune des coordonnees des autres bateaux), false sinon
		l=len(self.tabBats)
		trouvee=False
		if not(self.getBateaux()==[]):
			for i in range(0,l):
				b = self.getBateaux()[i]
				t= bateau.taille()
				bt = bateau.getTabCords()
				j=0
				while(not(trouvee) and (j<t)):
					x=bt[j][0]
					y=bt[j][1]
					trouvee = (b.estOccupee(x,y))
					j=j+1
		return trouvee

	def ajoutBateau(self, bateau):# Flotte*Bateau*int => Flotte
		#donnee: un objet de type bateau non vide, une flotte et le numero du bateau que l'on veut ajouter (entre 1 et 5)
		#resultat : la flotte avec le bateau ajoute a celle-ci si il ne se superpose pas avec un autre, erreur sinon. AJOUTER UN BATEAU A UNE FLOTTE COMPLETE RENVOIE UNE ERREUR
		if self.verifSuperpose(bateau):
			raise Exception("Le Bateau se superpose déjà avec un Bateau dans la flotte")
		elif len(self.tabBats)==5:
			raise Exception("La Flotte est complète")
		else:
			self.tabBats.append(bateau)

		return self

	def enVueF(self,x,y): #flotte*int*int => bool
		#donnee: une flotte de 5 bateaux et les coordonnees de tir x et y (entre 0 et 20)
		#resultat : true si un des bateaux est en vue et qu'aucun n'est touché , false sinon 
		if self.getBateaux()==[]:
			raise Exception("La Flotte est vide")
		elif (x<0 & x>21) or (y<0 & y>21):
			raise Exception("L'une des coordonnées est soit trop grande, soit négative")
		else:
			flotte=self.getBateaux()
			l=len(flotte)
			enVueF = False
			i =0
			if not(self.toucheFlotte(x,y)):
				while (i<l) & (not(enVueF)):
					enVueF = enVueF or flotte[i].enVueB(x,y)
					i=i+1
		return	enVueF

	def toucheFlotte(self,x,y): #Flotte*int*int=> bool
		#donnee: flotte de 5 bateaux et deux entiers (x,y) les coordonnees de tir 
		#resultat : true si un des bateaux de la flotte est touche, false sinon, erreur si la flotte est vide
		if self.getBateaux()==[]:
			raise Exception("La Flotte est vide")
		elif (x<0 & x>21) or (y<0 & y>21):
			raise Exception("L'une des coordonnées est soit trop grande, soit négative")
		else:
			flotte=self.getBateaux()
			l=len(flotte)
			toucheF = False
			i =0
			while (i<l) & (not(toucheF)):
				toucheF = toucheF or flotte[i].estOccupee(x,y)
				i=i+1
		return	toucheF
