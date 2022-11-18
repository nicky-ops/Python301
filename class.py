class Animals:
    this_as_a_property = "Something sweet"

the_animal = Animals()
print(the_animal.this_as_a_property)

class Alibaba:
    items = {
        "Name":"Jigsaw",
        "Weight" : 56,
        "qty": 40

    }
    participants = ["Knae","Kalob", "Milkshake", "Ndich","Humphrey"]

    # Private Property
    awards = {
        "First":"Gold",
        "Second": "Silver",
        "Third": "Bronze"
    }

    def remove_participants(self, name):
        self.participants.remove(name)
        return self.participants
    
    @property
    def awards_lst(self):
        return self.awards["First"]


check = Alibaba()
award = check.awards_lst
print(award)
updated_lst = check.remove_participants('Humphrey')
print(updated_lst)

# print(check.items['Name'])
# print(check.participants[1])
