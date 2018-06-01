#coding:utf8
def test_unitaires():
	test_bateau()
	test_joueur()
	test_partie()

def test_bateau():
	while True:
		try :
			cb=creer_bateau([(10,3),(10,4)])				#Retourne une erreur : x<0 or y<0
			print(" Test creation bateau avec parametres correctes OK")
			break
		except:
			print("ERROR : Test creation bateau avec parametres correctes FAILURE")
	while True:								#Ne retourne pas d'erreur
		try :
			cbError=creer_bateau([(-10,3),(-10,4)])					#Retourne une erreur : x<0 or y<0
			print("ERROR : Test creation bateau hors grille FAILURE")
			break
		except:
			print("Test creation bateau hors grille OK ")

	while True:								
		try :
			cbError2=creer_bateau([(21,3),(21,4)])							#Retourne une erreur : x>20 or y>20
			print("ERROR : Test (2) creation bateau hors grille FAILURE")
			break
		except:
			print("Test (2) creation bateau hors grille OK ")


	while True:								
		try :
			cbError3=creer_bateau([(1,3),(5,4)])							#Retourne une erreur : cases non adjacentes
			print("ERROR : Test creation bateau avec cases non adjacentes FAILURE")
			break
		except:
			print("Test creation bateau avec cases non adjacentes OK ")

	while True:								
		try :
			cbError4=creer_bateau([(1,3),(1,4),(1,5),(1,6),(1,7),(1,8)])	#Retourne une erreur : bateau trop grand
			print("ERROR : Test creation bateau trop grand FAILURE")
			break
		except:
			print("Test creation bateau trop grand OK ")

	while True:								
		try :
			cbError5=creer_bateau()											#Retourne une erreur : bateau vide
			print("ERROR : Test creation bateau vide FAILURE")
			break
		except:
			print("Test creation bateau vide OK ")

	cb2=creer_bateau([(2,2),(2,3)])									
	cb3=creer_bateau([(2,2),(3,2)])
	while True:								
		try :
			sb=(superposes_bat(cb,cb2)==False)								#Ne retourne pas d'erreur									
			if(sb):
				print("Test Superposition bateau OK")
			else:
				print("ERROR : Test Superposition bateau FAILURE ")
			break
		except:
			print("ERROR : Test Superposition bateau FAILURE ")

	while True:								
		try :
			sb2=(superposes_bat(cb2,cb3)==True)								#Ne retourne pas d'erreur
			if(sb2):
				print("Test Superposition bateau OK")
			else:
				print("ERROR : Test Superposition bateau FAILURE")
			break
		except:
			print("ERROR : Test Superposition bateau FAILURE")

	while True:								
		try :
			et=(est_touche(cb,10,3)==True)	
			if(et):												#Ne retourne pas d'erreur 
				print("Test est_touche sur case de bateau OK")
			else:								#Ne retourne pas d'erreur
				print("ERROR: Test est_touche sur case de bateau FAILURE ")
			break
		except:
			print("ERROR: Test est_touche sur case de bateau FAILURE ")

	while True:								
		try :
			et3=(est_touche(cb,10,8)==False)
			if(et3):												#Ne retourne pas d'erreur 
				print("Test est_touche avec case n'appartenant pas a un bateau OK")
			else:
				print("ERROR: Test est_touche avec case n'appartenant pas a un bateau FAILURE  ")
			break
		except:
			print("ERROR: Test est_touche avec case n'appartenant pas a un bateau FAILURE  ")

	while True:								
		try :
			etError=est_touche(cb,-1,3)										#Retourne une erreur : x<0 or y<0
			print("ERROR: Test est_touche avec x inferieur à 0 FAILURE ")
			break
		except:
			print("Test est_touche avec x inferieur à 0 OK ")

	while True:								
		try :
			etError5=est_touche(cb,1,-3)										#Retourne une erreur : x<0 or y<0
			print("ERROR: Test est_touche avec y inferieur à 0 FAILURE ")
			break
		except:
			print("Test est_touche avec y inferieur à 0 OK ")

	while True:								
		try :
			etError2=est_touche(cb,42,3)									#Retourne une erreur : x>20 or y>20
			print("ERROR: Test est_touche avec x superieur a 20 FAILURE ")
			break
		except:
			print("Test est_touche avec x superieur a 20 OK ")

	while True:								
		try :
			etError6=est_touche(cb,42,3)									#Retourne une erreur : x>20 or y>20
			print("ERROR: Test est_touche avec y superieur a 20 FAILURE ")
			break
		except:
			print("Test est_touche avec y superieur a 20 OK ")

	while True:								
		try :
			etError3=est_touche(bateauVide,1,3)								#Retourne une erreur : bateau vide
			print("ERROR: Test est_touch avec bateau vide FAILURE ")
			break
		except:
			print("Test est_touch avec bateau vide OK ")

	ct=cb 															#Ne retourne pas d'erreur
	while True:								
		try :
			cb=appliquer_degats(cb,10,3)									#Ne retourne pas d'erreur
			print("Test appliquer_degats sur avec bonne coord et bon bateau OK")
			break
		except:
			print("ERROR: Test appliquer_degats sur avec bonne coord et bon bateau FAILURE  ")
	
	cb=appliquer_degats(cb,10,4)									
	ct=appliquer_degats(ct,10,3)									#Ne retourne pas d'erreur
	while True:								
		try :
			ct=appliquer_degats(ct,10,3)									#Retourne une erreur : la case a déjà été touchée
			print("ERROR: Test de tir sur case deja touché grace à appliquer_degats FAILURE ")
			break
		except:
			print("Test de tir sur case deja touché grace à appliquer_degats OK ")


	while True:								
		try :
			adError=appliquer_degats(cb,10,25)								#Retourne une erreur : x>20 or y>20
			print("ERROR: Test appliquer degats avec y superieur a 20 FAILURE ")
			break
		except:
			print("Test appliquer degats avec y superieur a 20 OK ")

	while True:								
		try :
			adError3=appliquer_degats(cb,30,15)								#Retourne une erreur : x>20 or y>20
			print("ERROR: Test appliquer degats avec x superieur a 20 FAILURE ")
			break
		except:
			print("Test appliquer degats avec x superieur a 20 OK ")

	while True:								
		try :
			adError2=appliquer_degats(cb,10,-1)								#Retourne une erreur : x<0 or y<0
			print("ERROR: Test appliquer_degats avec y inferieur a 0 FAILURE ")
			break
		except:
			print("Test appliquer_degats avec y inferieur a 0 OK ")

	while True:								
		try :
			adError4=appliquer_degats(cb,-10,1)								#Retourne une erreur : x<0 or y<0
			print("ERROR: Test appliquer_degats avec x inferieur a 0 FAILURE ")
			break
		except:
			print("Test appliquer_degats avec x inferieur a 0 OK ")


	while True:								
		try :
			ec=(est_coule(cb)==True)										#Ne retourne pas d'erreur
			print("Test est_coulé avec bateau coulé OK")
			break
		except:
			print("ERROR: Test est_coulé avec bateau coulé FAILURE  ")

	while True:								
		try :
			ec2=(est_coule(ct)==False)										#Ne retourne pas d'erreur
			print("Test est_coulé avec bateau non coulé OK")
			break
		except:
			print("ERROR: Test est_coulé avec bateau non coulé FAILURE  ")

	while True:								
		try :
			ecErreur=est_coule(bateauVide)									#Retourne une erreur : le bateau est vide
			print("ERROR: Test est_coulé avec bateau vide FAILURE ")
			break
		except:
			print("Test est_coulé avec bateau vide OK ")


	while True:								
		try :
			ev=(est_en_vue(ct,10,11)==True)									#Ne retourne pas d'erreur
			print("Test est_en_vue avec coordonée en vue OK")
			break
		except:
			print("ERROR: Test est_en_vue avec coordonée en vue FAILURE  ")


	while True:								
		try :
			ev2=(est_en_vue(ct,11,6)==False)								#Ne retourne pas d'erreur
			print("Test est_en_vue avec coordonée ne donnaant pas en vue sur le bateau en param OK")
			break
		except:
			print("ERROR: Test est_en_vue avec coordonée ne donnaant pas en vue sur le bateau en param FAILURE  ")


	while True:								
		try :
			ev3=(est_en_vue(cb,1,3)==False)									#Ne retourne pas d'erreur
			print("Test est_en_vue avec coordonnée qui etait en vue sur une case mais qui a été détruite OK")
			break
		except:
			print("ERROR: Test est_en_vue avec coordonnée qui etait en vue sur une case mais qui a été détruite FAILURE  ")

	while True:								
		try :
			ev4=est_en_vue(cb,10,25)								#Retourne une erreur : x>20 or y>20
			print("ERROR: Test est_en_vue avec y superieur a 20 FAILURE ")
			break
		except:
			print("Test  est_en_vue  avec y superieur a 20 OK ")

	while True:								
		try :
			ev5=est_en_vue(cb,30,15)								#Retourne une erreur : x>20 or y>20
			print("ERROR: Test  est_en_vue  avec x superieur a 20 FAILURE ")
			break
		except:
			print("Test  est_en_vue  avec x superieur a 20 OK ")

	while True:								
		try :
			ev6=est_en_vue(cb,10,-1)								#Retourne une erreur : x<0 or y<0
			print("ERROR: Test est_en_vue avec y inferieur a 0 FAILURE ")
			break
		except:
			print("Test est_en_vue avec y inferieur a 0 OK ")

	while True:								
		try :
			ev7=est_en_vue(cb,-10,1)								#Retourne une erreur : x<0 or y<0
			print("ERROR: Test est_en_vue avec x inferieur a 0 FAILURE ")
			break
		except:
			print("Test est_en_vue avec x inferieur a 0 OK ")

	while True:								
		try :
			evError=est_en_vue(bateauVide,1,4)								#Retourne une erreur : le bateau est vide
			print("ERROR: Test est_en_vue avec un bateau vide FAILURE ")
			break
		except:
			print("Test est_en_vue avec un bateau vide OK ")

	while True:								
		try :
			evError2=est_en_vue(ct,10,4)										#Retourne une erreur : la case a été touchée
			print("ERROR: Test Est_en_vue avec une case deja touché FAILURE ")
			break
		except:
			print("Test Est_en_vue avec une case deja touché OK ")

def test_joueur():
	b1=creer_bateau([(1,1)])										#Ne retourne pas d'erreur
	b2=creer_bateau([(2,2),(2,3)])									#Ne retourne pas d'erreur
	b3=creer_bateau([(3,1),(4,1),(5,1)])							#Ne retourne pas d'erreur
	b3b=creer_bateau([(15,14),(16,14),(17,14)])						#Ne retourne pas d'erreur
	b4=creer_bateau([(3,2),(4,2),(5,2),(6,2)])						#Ne retourne pas d'erreur
	b5=creer_bateau([(17,4),(17,3)])								#Ne retourne pas d'erreur
	b6=creer_bateau([(2,2),(3,2)])									#Ne retourne pas d'erreur
	while True:								
		try :
			j1=creer_joueur([b1,b2,b3,b3b,b4])						#Ne retourne pas d'erreur
			print("Test creer_joueur avec de bonnes coordonnées OK")
			break
		except:
			print("ERROR: Test creer_joueur avec de bonnes coordonnées FAILURE  ")

	while True:								
		try :
			jError=creer_joueur([b1,b2,b3,b3b,b4,b5])						#Retourne une erreur : le joueur a trop de bateaux
			print("ERROR: Test creer_joueur avec trop de bateaux FAILURE ")
			break
		except:
			print("Test creer_joueur avec trop de bateaux OK ")

	while True:								
		try :
			jError2=creer_joueur(tabvide)									#Retourne une erreur : le joueur n'a pas de bateaux
			print("ERROR: Test creer_joueur avec aucun bateaux FAILURE ")
			break
		except:
			print("Test creer_joueur avec aucun bateaux OK ")

	while True:								
		try :
			jError3=creer_joueur([b2,b6])									#Retourne une erreur : les bateaux se superposent
			print("ERROR: creer_bateau avec des bateaux qui se superposent FAILURE ")
			break
		except:
			print("creer_bateau avec des bateaux qui se superposent OK ")
	

def test_partie():
	gbj=(get_bateaux_joueur(j1)==[b1,b2,b3,b3b,b4])					#Ne retourne pas d'erreur	
	jp=(joueur_a_perdu(j1)==False)									#Ne retourne pas d'erreur
	ja=creer_joueur([b1,b2])										#Ne retourne pas d'erreur
	tabBat=get_bateaux_joueur(ja)									#Ne retourne pas d'erreur
	appliquer_degats(tabBat[0],1,1)									#Ne retourne pas d'erreur
	appliquer_degats(tabBat[1],2,2)									#Ne retourne pas d'erreur
	appliquer_degats(tabBat[1],2,3)									#Ne retourne pas d'erreur
	jp2=(joueur_a_perdu(ja)==True)									#Ne retourne pas d'erreur
	j1=creer_joueur([b1,b2,b3,b3b,b4])								#Ne retourne pas d'erreur
	j2=creer_joueur([b1,b2,b3,b3b,b4])								#Ne retourne pas d'erreur	

	while True:								
		try :
			cp=creer_Partie([j1,j2])										#Ne retourne pas d'erreur
			print("Test creer_Partie avec de bon parametres OK")
			break
		except:
			print("ERROR: Test creer_Partie avec de bon parametres FAILURE  ")

	while True:								
		try :
			cpError=creer_Partie([j1,j1])									#Retourne une erreur : On a deux fois le meme joueur
			print("ERROR: Test creer_Partie avec deux fois le meme joueur FAILURE ")
			break
		except:
			print("Test creer_Partie avec deux fois le meme joueur OK ")	

	while True:								
		try :
			cpError2=creer_Partie([j1,j2,ja])								#Retourne une erreur : On a trop de joueurs 
			print("ERROR: Test creer_Partie avec trop de joueurs FAILURE ")
			break
		except:
			print("Test creer_Partie avec trop de joueurs OK ")	


	while True:								
		try :
			fp=(fin_partie(cp)==TRUE)
			if(fp):												#Ne retourne pas d'erreur 
				print("Test fin_Partie avec de bon parametres OK")
			else:
				print("ERROR: Test fin_Partie avec de bon parametres FAILURE  ")
			break
		except:
			print("ERROR: Test fin_Partie avec de bon parametres FAILURE  ")


	while True:								
		try :
			fpError=fin_partie(partievide)									#Retourne une erreur : la partie ne comporte pas de joueurs		
			print("ERROR: Test fin_partie sur une partie sans joueurs FAILURE ")
			break
		except:
			print("Test fin_partie sur une partie sans joueurs OK ")	

	
	
	

				
								

