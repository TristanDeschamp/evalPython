class Livre:
	"""
	Classe représentant un livre avec un titre et un auteur
	Cette classe sert de base pour d'autres type de livres 
	"""
	def __init__(self, titre: str, auteur: str):
		self._titre = titre
		self._auteur = auteur

	@property
	def titre(self) -> str:
		""" Retourne le titre de du livre """
		return self._titre

	@property
	def auteur(self) -> str:
		""" Retourne l'auteur du livre """
		return self._auteur

	def afficher_info(self) -> str:
		""" Retourne une chaîne de caractères avec les informations du livre. """
		return f"Titre : {self._titre}, Auteur : {self._auteur}"

	def __str__(self) -> str:
		return self.afficher_info()

	def __repr__(self) -> str:
		return f"Livre(titre={self._titre}, auteur={self._auteur})"


class LivreEmpruntable(Livre):
	"""
   Classe représentant un livre empruntable, hérite de Livre.
   Ajoute la gestion de la disponibilité d'un livre.
   """
	def __init__(self, titre: str, auteur: str):
		super().__init__(titre, auteur) # Appelle le constructeur de la classe mère Livre
		self._disponible = True # Par défaut, le livre est disponible

	@property
	def disponible(self) -> bool:
		"""Retourne True si le livre est disponible, False sinon."""
		return self._disponible

	def emprunter(self) -> None:
		"""
		Permet d'emprunter le livre s'il est disponible.
      Sinon, une exception est levée.
      """
		if not self._disponible:
			raise ValueError(f"Le livre '{self.titre}' est déjà emprunté.")
		self._disponible = False
		print(f"Le livre '{self.titre}' a été emprunté.")

	def retourner(self) -> None:
		"""
		Permet de retourner un livre emprunté.
		Si le livre est déjà disponible, une exception est levée.
      """
		if self._disponible:
			raise ValueError(f"Le livre '{self.titre}' est déjà disponible.")
		self._disponible = True
		print(f"Le livre '{self.titre}' a été retourné.")

	def afficher_info(self) -> str:
		dispo = "Disponible" if self._disponible else "Indisponible"
		return f"{super().afficher_info()}, Disponibilité : {dispo}"

	def __str__(self) -> str:
		return self.afficher_info()

	def __repr__(self) -> str:
		return f"LivreEmpruntable(titre={self.titre}, auteur={self.auteur}, disponible={self._disponible})"


# Exemple d'utilisation
livre1 = Livre("1984", "George Orwell")
livre2 = LivreEmpruntable("Le Petit Prince", "Antoine de Saint-Exupéry")

print(livre1)  # Utilise __str__
print(livre2)

livre2.emprunter()
print(livre2)

try:
	livre2.emprunter()  # Provoque une erreur
except ValueError as e:
	print(e)

livre2.retourner()
print(livre2)

try:
	livre2.retourner()  # Provoque une erreur
except ValueError as e:
	print(e)
