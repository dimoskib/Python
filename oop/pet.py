class Pet:
	allowed = ['cat','dog','fish','rat']
	def __init__(self, name, species):
		allowed = ['cat','dog','fish','rat']
		if species not in allowed:
			raise ValueError(f"You can't have {self.species} pet.")
		self.name = name
		self.species = species

cat = Pet("Blue","cat")
dog = Pet("Wyatt", "dog")