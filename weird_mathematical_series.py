class Error(Exception):
	""" Classe de base pour exceptions """
	pass

class StrictementPositif(Error):
	""" Appelé quand le nombre saisi n'est pas strictement positif """
	pass

"""
	fonction récursive
	paramètres d'entrée :
		somme  : somme initialement vallant 0 et qui est ensuite récursivement calculée jusqu'à valloir 1 ou 4
		nombre : nombre étudié venant de la boucle 'for' pour lequel on récupère le reste de la division euclidienne
			     nombre est ensuite à chaque boucle while divisé par 10. On arrêter l'itération sur le nombre n quand la partie 
			     entière de la division euclidienne de n par 10 ne vaut plus que 0
	paramètre renvoyé:
		somme  : résultat final de la somme : 1 ou 4
"""

# somme est définie comme paramètre par défaut et initialisée à 0
def suite_inconnue(nombre, somme = 0):
	# réalisation du calcul de la somme tant que nombre est non nul
	while nombre != 0:
		somme = somme + (nombre % 10)**2
		nombre = nombre // 10
	# la somme vaut 1 ou 4, on retourne la somme calculée
	if somme == 1 or somme == 4:
		return somme
	# somme ne vaut ni 1 ni 4, utilisation de la récursivité
	# passage par copie du résultat précédent 'somme' dans le paramètre 'nombre'
	else:
		return suite_inconnue(somme)

# déclaration des vecteurs qui vont récupérer les résultats de la fonction récursive
# vecteur pour la somme finissant à 1
vect1 = []
# vecteur pour la somme finissant à 4
vect4 = []

# contrôle de la saisie, le nombre doit être strictement positif
# création d'exceptions personnalisées et affichage en Français
while True:
	try:
		valeurSeuil = int(input("Entrez un nombre > 0 = ").strip('n'))
		if valeurSeuil < 1:
			raise StrictementPositif
		break
	except ValueError:
		print("Entrez SVP un nombre et non un caractère")
	except StrictementPositif:
		print("Le nombre saisi doit être strictement supérieur à 0")

# les valeurs étudiées seront de 'valeurEtude' à 'valeurSeuil' (préalablement saisie et contrôlée)
for valeurEtude in range(1, valeurSeuil + 1):
	somme = suite_inconnue(valeurEtude)
	# la fonction récursive retourne 1, on ajoute en fin du vecteur vect1[] le nombre étudié 'valeurEtude'
	if somme == 1:
		vect1.append(valeurEtude)
	# la fonction récursive retourne 4, on ajoute en fin du vecteur vect4[] le nombre étudié 'valeurEtude'
	else:
		vect4.append(valeurEtude)

# création des chaines de caractères finales 
# concaténation de 'valeurEtude' transtypée (passage d'entier à chaine de caractères) avec un espace
# cas particulier si l'on ne rentre que 1 comme 'valeurEtude'
if len(vect1) == 1:
	maChaineV1 = str(vect1[0])
# cas général pour vect1[], initialisation de maChaineV1 à la première valeur contenue dans le vecteur vect1[]
else:
	maChaineV1 = str(vect1[0])
	for i in range(1, len(vect1)):
		maChaineV1 += ' ' + str(vect1[i])

# cas particulier si l'on ne rentre que 1 comme 'valeurEtude'
if len(vect4) == 0:
	maChaineV4 = ''
# cas particulier si l'on ne rentre que 2 comme 'valeurEtude'
elif len(vect4) == 1:
	maChaineV4 = str(vect4[0])
# cas général pour vect4[], initialisation de maChaineV4 à la première valeur contenue dans le vecteur vect4[]
else:
	maChaineV4 = str(vect4[0])
	for i in range(1, len(vect4)):
		maChaineV4 += ' ' + str(vect4[i])

# affichage des résultats sous forme de chaine de caractère
print("Liste des entiers qui arrivent à 1 = ", maChaineV1)
print("Liste des entiers qui arrivent à 4 = ", maChaineV4)