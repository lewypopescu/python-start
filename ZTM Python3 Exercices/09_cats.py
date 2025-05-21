# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
catsData = [
    Cat("Whiskers", 8),
    Cat("Mittens", 4),
    Cat("Shadow", 2)
]


# 2 Create a function that finds the oldest cat
def find_oldest_cat(cats):
    oldest_cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat


# 3 Print out: "The oldest cat ... is x years old.". x will be the oldest cat age by using the function in #2
oldest_cat = find_oldest_cat(catsData)
print(
    f"The oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old.")
