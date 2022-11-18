class Animal:
    def attributes(self):
        return "An animal has 4 limbs"


    def cold_blooded(self,number):
        if number == 1:
            return "The animal is Cold Blooded"
        else:
            return 'The animal is warm blooded'

    def eat(self):
        pass
    def speak(self):
        raise NotImplementedError

class Cat(Animal):
    @property
    def sound(self):
        return "A Cat Purrrrs!"
class Human(Animal):

    @property
    def sound(self):
        return "A human speaks"

cat = Cat()
human = Human()

body = human.cold_blooded(1)
sound = human.speak()

print(body)
print(sound)