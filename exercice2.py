def trouver_max():
	""" Demande à l'utilisateur d'entrer 5 nombres entiers et affiche le plus grand """
	nombres = [int(input(f"Entrez un nombre ({i+1}/5) : ")) for i in range(5)]
	print(f"Le plus grand nombre est : {max(nombres)}")

trouver_max()