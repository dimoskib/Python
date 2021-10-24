class User:
	 def __init__(self, first, last, age):
	 	self.first = first
	 	self.last = last
	 	self.age = age

	 def full_name(self):
	 	return f"{self.first} {self.last}"


user1 = User("Joe", "Vlofis", 32)
user2 = User("Blanca", "Lopez", 30)
print(user2.full_name())