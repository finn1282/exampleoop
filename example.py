class Animal:
	
	def __init__(self, species, age, name):
		self.species = species
		self.age = age
		self.name = name

	def nameGetter(self):
		return self.name

class Elephant(Animal):

	def __init__(self,species, age, name ,feetAmount):
		super().__init__(species, age, name)
		self.feetAmount = 4

	def feetGetter(self):
		return self.feetAmount
	
	super().nameGetter()


if __name__=="__main__":
	cat = Animal("cat", 20, "bob")

	print(cat.nameGetter())