class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		if age >= 0:
			self._age = age
		else:
			self._age = 0


	@property
	def age(self):
		return self._age
		
	@age.setter
	def age(self,value):
		if value >=0:
			self._age=value
		else:
			raise ValueError("age can't be negative")



jane = Human("Jane", "Goodall", 49)
print(jane.age)
