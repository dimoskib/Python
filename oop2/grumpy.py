class GrumpyDict(dict):
	def __repr__(self):
		print("NONE OF YOUR business") 
		return super().__repr__()

	def __missing__(self, key):
		print(f"You want {key} ? well it aint here!")

	def __setitem__(self, key, value):
		print("Ok fine...")
		super().__setitem__(key,value)

data = GrumpyDict({"first":"Tom","animal":"cat"})
print(data)
data['city'] = 'Tokyo'
print(data)