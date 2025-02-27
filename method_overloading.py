class animal:
    def sounds(self):
        print("make sounds like a animal")
class dog(animal):
    def sounds(self):
        print("bow bow")
class cat(animal):
    def sounds(self):
        print("meow meow")

animal=cat()
animal.sounds()