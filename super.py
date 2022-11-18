class Animal:
    def attributes(self):
        return "An animal has 4 limbs"


    def cold_blooded(self,number):
        if number == 1:
            return "The animal is Cold Blooded"
        else:
            return 'The animal is warm blooded'

    def eat(self, animal="gazelle"):
        print( "I want to eat a ", animal)

class Cat(Animal):
    @property
    def sound(self):
        return "A Cat Purrrrs!"
class Human(Animal):

    @property
    def sound(self):
        return "A human speaks"

    def eat(self, animal):
        super().eat(animal)
        print('I have finished eating,',animal)

cat = Cat()
human = Human()

body = human.cold_blooded(1)
eat = human.eat("Spider")

print(body)
print(eat)