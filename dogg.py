# create class

class Dog:

# class attribute

    species = "canines"

# instance attribute

    def __init__(self, name, age,breed):

        self.name = name

        self.age = age
        self.breed = breed 

# instantiate the Parrot class

rocky = Dog("Rocky", 10,"Alsatain")

jenny = Dog("Jenny", 7,"Rottweiler")

# access the class attributes

print("Rocky is a {}".format(rocky.species))

print("Jenny is also a {}".format(jenny.species))

# access the instance attributes

print("{} is {} years old".format( rocky.name, rocky.age))

print("{} is {} years old".format( jenny.name, jenny.age))
print("{} is {} breed".format(rocky.name,rocky.breed))
print("{} is {} breed".format(jenny.name,jenny.breed))