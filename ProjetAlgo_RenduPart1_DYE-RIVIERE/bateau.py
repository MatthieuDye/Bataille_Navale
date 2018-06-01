#coding:utf8
															########	Bateau		#########
class Bateau(object):

 def __init__(tabCaseBateau):
 	#creer_bateau [(int,int)] -> Bateau 					#Crée et initialise un Bateau
															#Prec : tous les couples de coordonnées sont compris entre 0 et 20

def est_touche (bateau,x,y): 
	#est_touché Bateau x int x int -> bool					#Vrai si le couple de int correspond à l'une des cases du Bateau
															#Prec : Les deux int sont compris entre 0 et 20 & Bateau initialisé
															#Prop : est_touche (bateau,x,y) => (x,y) in bateau
	return

def est_coule (bateau): 
	#est_coulé Bateau -> bool								#Vrai si toutes les coordonnées du bateau ont été touchées
															#Prec : Bateau initialisé
															#Prop : est_coule (bateau) => quelque soit (x,y) in bateau, est_touché(bateau,x,y)
	return

def est_en_vue (bateau,x,y): 
	#est_en_vue Bateau x int x int -> bool					#Vrai si au moins l'une des coordonnées du couple de int correspond à l'une de celles du Bateau
															#Prec : Les deux int sont compris entre 0 et 20 & Bateau initialisé
															#Prop : est_en_vue (bateau,x,y) => not(est_touché(bateau,x,y) & (3 z tel que (x,z) in bateau or (y,z) in bateau
	return 			 

def appliquer_degats (bateau,x,y): 
	#appliquer_degats Bateau x int x int -> Bateau			#Marque la partie du bateau de coordonnées le couple de int en paramètre, afin qu'elle ne puisse pas être redétruite ulterieurement
															#Prec : est_touché(Bateau,a,b)=True
															#       Les deux int sont compris entre 0 et 20 & Bateau initialisé
															#Post : est_touché(Bateau,a,b)=False
															#		est_en_vue(Bateau,a,b)=False
															#Prop :	est_touche(bateau,x,y) => appliquer_degats(bateau,x,y)
	return 	

def superposes_bat (bateau1,bateau2):
	#superposes_bat Bateau x Bateau -> bool					#Desc : Vérifie si deux bateaux sont superposés. Retourn True si c'est le cas.
															#Prec : Les deux bateau sont initialisés 
															#Prop : superposes_bat(bat1,bat2) => 3 (x,y) tel que (x,y) in bat1 & (x,y) in bat2
	return