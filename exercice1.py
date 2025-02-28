def calcul_mental():
	""" Demande à l'utilisateur d'entrer le montant total de ses achats et applique une remise si nécessaire """
	montant = float(input("Entrez le montant total de vos achats : "))
	if montant > 100:
		montant *= 0.9 # Appliquer une réduction de 10%
		print(f"Vous bénéficiez d'une remise de 10%. Montant à payer : {montant:.2f}€")
	else:
		print(f"Pas de remise. Montant à payer : {montant:.2f}€")

calcul_mental()