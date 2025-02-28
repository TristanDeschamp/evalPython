def distributeur_billets():
	""" Simule un distributeur de billets permettant de retirer un montant valide """

	while True: # Boucle infinie jusqu'à ce que l'utilisateur entre un montant valide
		try:
			montant = int(input("Entrez le montant à retirer : "))

			# Vérification si le montant est un multiple de 10
			if montant % 10 != 0:
				print("Le montant doit être un multiple de 10.")
				continue # Demande une nouvelle saisie

			# Vérification si le montant dépasse la limite de retrait (500€)
			if montant > 500:
				print("Le montant ne peut pas dépasser 500€.")
				continue

			# Calcul du nombre de billets de 50€
			billets_50 = montant // 50
			montant %= 50 # Reste après avoir retiré les billets de 50€

			billets_20 = montant // 20
			montant %= 20 # Reste après avoir retiré les billets de 20€

			billets_10 = montant // 10 # Le reste doit être forcément 0

			print("Billets distribués :")
			if billets_50 > 0:
				print(f"- {billets_50} billet(s) de 50€")
			if billets_20 > 0:
				print(f"- {billets_20} billet(s) de 20€")
			if billets_10 > 0:
				print(f"- {billets_10} billet(s) de 10€")
			break # Sortie de la boucle après une saisie correcte
		except ValueError:
			# Gestion d'erreur si l'utilisateur entre autre chose qu'un nombre entier
			print("Entre un montant valide sous forme de nombre entier.")

distributeur_billets()