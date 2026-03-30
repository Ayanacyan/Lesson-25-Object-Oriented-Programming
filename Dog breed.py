class Dog:
    breed1="golden retriver"
    breed2="Labrador"

    def __init__(self, name, age):
        self.name=name
        self.age=age

coco=Dog("Coco", 5)
oreo=Dog("Oreo",8)

print("{} is a {}".format(coco.name, coco.breed1))
print("{} is a {}".format(oreo.name, oreo.breed2))

print("{} is {} years old".format(coco.name, coco.age))
print("{} is {} years old".format(oreo.name, oreo.age))