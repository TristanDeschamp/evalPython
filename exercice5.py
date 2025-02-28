def distributeur_billets():
	while True:
		montant = int(input("Entrez le montant à retirer : "))

		if montant % 10 != 0:
			print("Le montant doit être un multiple de 10.")
			continue
		if montant > 500:
			print("Le montant ne peut pas dépasser 500€.")
			continue

		billets_50 = montant // 50
		montant %= 50

		billets_20 = montant // 20
		montant %= 20

		billets_10 = montant // 10

		print("Billets distribués :")
		if billets_50 > 0:
			print(f"- {billets_50} billet(s) de 50€")
		if billets_20 > 0:
			print(f"- {billets_20} billet(s) de 20€")
		if billets_10 > 0:
			print(f"- {billets_10} billet(s) de 10€")
		break

distributeur_billets()