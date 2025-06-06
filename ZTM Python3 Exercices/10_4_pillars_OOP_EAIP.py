class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 1 Add nother Cat


class Fufy(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [
    Simon("Sim", 2),
    Sally("Sal", 4),
    Fufy("Fuf", 6)
]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()

# 5 Output all of the cats singing using the my_pets instance
for cat in my_pets.animals:
    print(cat.sing("Meow"))

# 6 Output the oldest cat
def find_oldest_cat(cats):
    oldest_cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat


oldest_cat = find_oldest_cat(my_pets.animals)
print(
    f"The oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old.")

custom_sounds = ["Meowwww!", "Purrrrr...", "Miauuu!"]

for cat, sound in zip(my_cats, custom_sounds):
    print(f'{cat.name} sings: {cat.sing(sound)}')
