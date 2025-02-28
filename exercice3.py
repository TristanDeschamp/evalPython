import re

def verifier_mot_de_passe(mot_de_passe: str) -> str:
	""" Vérifie si un mot de passe est valide ou non, sans boucle """
	# Utilisation d'une expression régulière pour vérifier les conditions (un peu maso, je le sais)
	if len(mot_de_passe) >= 8 and re.search(r'\d', mot_de_passe):
		return "Mot de passe valide"
	return "Mot de passe invalide (doit contenir au moins 8 caractères et un chiffre)"

mot_de_passe = input("Entrez un mot de passe : ")
print(verifier_mot_de_passe(mot_de_passe))