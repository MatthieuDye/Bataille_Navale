#! usr/bin/python 
#-*- coding: utf-8 -*-
import sys
from Flotte import *
from Bateau import *


def testU(): 
	print("TESTS CLASSE BATEAU")
	#tests bateau
	Bateau1=Bateau(2,5,"x",3) #renvoie un bateau appartenant à la grille 
	Bateau2=Bateau(7,12,"y",4) #renvoie un bateau appartenant à la grille 
	print("test creer bateau")
	#print(Bateau(-1,8,"y",4)) #erreur car  origineX negative
	#print(Bateau(8,7,"x",5)) #erreur car taille >4 
	#print(Bateau(8,-5,"y",1)) #erreur car origineY negative
	#print(Bateau(7,7,"z",3)) #erreur car orientation differente de x ou y 
	#print(Bateau(20,20,"x",3))#erreur car le bateau sort de la grille 

	print("test taille")
	print(Bateau1.taille()) # renvoie 3 la taille du bateau 
	#pas d'erreur possible sur taille car creerBateau renvoie un bateau de taille comprise entre 1 et 4 
	
	print("test estoccupe")
	""" les erreurs détectées sur le test estOccupe sont des erreurs de type "conventionnel" c'est à dire correspondent uniquement à la manière d'interpréter le test 
	#(ils veulent pouvoir compter les true, c'est à dire que le test a fonctionné alors que notre test renvoie false)"""
	print((Bateau2.estOccupee(10,20))==False) #renvoie false : le bateau n'occupe pas la case 
	#print(Bateau1.estOccupee(-1,20)) # erreur les X entrés ne sont pas valides 
	#print(Bateau1.estOccupee(10,-5)) #erreur les Y entrés ne sont pas valides 
	#print(Bateau1.estOccupee(10,21)) # erreur les Y entrés ne sont pas valides 
	#print(Bateau2.estOccupee(40,20)) # erreur les X entrés ne sont pas valides
	""""il y avait bien une erreur de copie (estOccupe(10,20) devient estOccupe(40,20)) """
	print(Bateau(10,18,"y",3).estOccupee(10,20)) # renvoie true : le bateau occupe bien la case (10,20)

	print("test touche")
	#print(Bateau1.touche(18,19))# renvoie une erreur 
	print(Bateau(3,5,"x",4).touche(4,5))# renvoie le bateau modifié : il n'existe plus sur la case touchee
	#print(Bateau2.touche(-3,5))# renvoie erreur 
	#print(Bateau2.touche(4,-5))# renvoie erreur 

	print("test couleB")
	""" les erreurs détectées sur le test estOccupe sont des erreurs de type "conventionnel" c'est à dire correspondent uniquement à la manière d'interpréter le test 
	#(ils veulent pouvoir compter les true, c'est à dire que le test a fonctionné alors que notre test renvoie false) """
	print((Bateau2.couleB())==False) #false, le bateau n'est pas coule
	print(Bateau1.tabCords) 
	print((Bateau1.touche(3,5).couleB())== False ) # false le bateau n'est touche que sur une case 
	print(Bateau(5,5,"y",2).touche(5,5).touche(5,6).couleB()) # renvoie true : le bateau est touche sur ses deux cases 

	print("test enVueB")
	#print(Bateau1.enVueB(-3,12)) # ERREUR coordonnee negative 
	#print(Bateau1.enVueB(2,-5)) # ERREUR coordonnee negative 
	print(Bateau1.tabCords)
	print(Bateau1.enVueB(2,5)==False) #FALSE CAR LA CASE APPARTIENT BIEN AU BATEAU
	print(Bateau1.enVueB(3,6)==False) #FALSE CAR LA CASE A ETE DETRUITE
	print(Bateau1.enVueB(5,5)) # true 
	print(Bateau2.enVueB(4,13)) # true 


	print("TESTS FLOTTE") 
	bat1=Bateau(0,0,"x",1)
	bat2=Bateau(1,1,"y",2)
	bat3=Bateau(9,10,"x",3)
	bat4=Bateau(13,13,"y",3)
	bat5=Bateau(15,20,"x",4)
	batSup=Bateau(13,11,"y",3)
	print(bat4.getTabCords())
	print(batSup.getTabCords())
	f1 = Flotte() #pas d'erreur possible 
	print(f1.getBateaux())
	#print("Le bateau 1 se superpose à un bateau déjà dans la flotte ? Résolu : "+str(f1.verifSuperpose(bat1)==False)) 
	print("test ajout bateau") 
	f1=f1.ajoutBateau(bat1) #ajoute bat 1
	#print("Le bateau 1 se superpose à un bateau déjà dans la flotte ? Résolu : "+str(f1.verifSuperpose(bat1)==True)) # True car le bateau a déja été ajouté a la flotte
	f1=f1.ajoutBateau(bat2) #ajoute bat 2
	f1=f1.ajoutBateau(bat3) #ajoute bat 3
	f1=f1.ajoutBateau(bat4) #ajoute bat 4
	#print("Le bateau Sup se superpose à un bateau déjà dans la flotte ? Résolu : "+str(f1.verifSuperpose(batSup)==True)) # True
	#f1=f1.ajoutBateau(batSup)#erreur : le bateau se superpose à un bateau deja existant
	f1=f1.ajoutBateau(bat5) #ajoute bat 5 
	

	print("test verifSuperpose")
	#f1=f1.ajoutBateau(bat1) # RETOURNE UNE ERREUR, LE BATEAU A DEJA ETE AJOUTE A LA FLOTTE, ET LA VERIFSUPERPOSE DE AJOUTBATEAU RENVOIE BIEN TRUE
	#print("Le bateau 1 se superpose à un bateau déjà dans la flotte ? Résolu : "+str(f1.verifSuperpose(bat1)==True)) # True car le bateau a déja été ajouté a la flotte
	#print("Le bateau 2 se superpose à un bateau déjà dans la flotte ? Résolu : "+str(f1.verifSuperpose(bat2)==True)) # True car le bateau a déja été ajouté a la flotte

	f2=Flotte()

	print("test toucheFlotte")
	print(f1.toucheFlotte(0,0)==True) # retourne true 
	#print(f2.toucheFlotte(0,0)) # retourne erreur car flotte vide 
	print(f1.toucheFlotte(20,20)==False) # false aucun bateau n'est touche 
	#print(f1.toucheFlotte(-2,3)) # erreur coordonnees mauvaises 
	#print(f1.toucheFlotte(2,-3))# erreur coordonnees mauvaises
	#print(f1.toucheFlotte(21,3)) # erreur coordonnees mauvaises 
	#print(f1.toucheFlotte(3,21)) # erreur coordonnees mauvaises 

	print("test enVueF")
	#print(f1.enVueF(-3,1)) # erreur mauvaise coordonnee 
	#print(f1.enVueF(3,-1)) #erreur mauvaise coordonnee 
	#print(f1.enVueF(1,111))#erreur mauvaise coordonnee 
	#print(f1.enVueF(300,11)) #erreur mauvaise coordonnee 
	print(f1.enVueF(15,14)==True)# true 
	print(f1.enVueF(0,0)==False) # false car la case est touchee donc ne peut etre envue 

	print("test couleF")
	f3=Flotte()
	f3=f3.ajoutBateau(bat1)
	print(f3.getBateaux())	
	bat1=bat1.touche(0,0)
	print(f3.getBateaux())

	#couleF=f2.couleF() # erreur flotte vide


	print(f3.couleF()==True) # retourne true car flotte de 5 bateaux coulés 
testU()