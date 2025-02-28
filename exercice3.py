def verifier_mot_de_passe(mot_de_passe: str) -> str:
	""" Vérifie si un mot de passe est valide ou non """
	if len(mot_de_passe) >= 8 and any(char.isdigit() for char in mot_de_passe):
		return "Mot de passe valide"
	else:
		return "Mot de passe invalide (doit contenir au moins 8 caractères et un chiffre)"

mot_de_passe = input("Entrez un mot de passe : ")
print(verifier_mot_de_passe(mot_de_passe))