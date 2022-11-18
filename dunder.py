class Animal:


    def __init__(self,fur_color):
        self.fur_color = fur_color


class Cow(Animal):

    def __init__(self, fur_color):
        super().__init__(fur_color)
        print(f"Fur color is {fur_color}")

    @property
    def sound(self):
        print("A cow Moos")


cow = Cow("Blue")
cow.sound