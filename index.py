from test import showErrors
nom=""
prenom=""
age=0
while True:
	print("Faites votre choix:\n 1- Taper votre nom \n 2- Taper vos prénoms\n 3- Taper votre age\n 4- Mes infos\n 5- QUITTER")
	a=int(input("taper un chiffre de 1 à 5 de votre choix: ")) #input considère l'élément entré comme étant une chaine de caractère
	if(a==5):
		print("QUITTER")
		break
	else:
		if(a==1):
			nom=input("entrer votre nom: ")
		elif(a==2):
			prenom=input("entrer vos prenoms: ")
		elif(a==3):
			age=int(input("entrer votre age: "))
		elif(a==4):
			erreurs=[] #tableau vide
			if len(nom)==0:
				erreurs.append('nom')

			if len(prenom)==0:
				erreurs.append('prenom')

			if age==0:
				erreurs.append('age')

			if (erreurs): #tester s'il y a klk choz a l'interieur du tableau
				print("Les champs suivant doivent etre remplies:")
				showErrors(erreurs)
				#for i in erreurs:
					#print("- ",i)
			else:
				infos={'nom:':nom, 'prenoms:':prenom, 'age:':age}
				print(infos)
