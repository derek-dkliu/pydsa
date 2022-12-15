from queue import QueueList, Queue

class AnimalShelter(QueueList):
    def enqueue(self, animal):
        self.add(animal)

    def dequeue_any(self):
        if self.empty():
            raise Exception("No animals available")
        return self.remove()

    def dequeue_dog(self):
        return self.dequeue_by_type(AnimalType.DOG)

    def dequeue_cat(self):
        return self.dequeue_by_type(AnimalType.CAT)

    def dequeue_by_type(self, type):
        if self.empty():
            raise Exception("No animals available")
        if self.peek().typeof(type):
            return self.remove()
        node = self.first
        while node.next:
            if node.next.val.typeof(type):
                animal = node.next.val
                node.next = node.next.next
                return animal
            node = node.next
        return None


class AnimalShelter2:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self.timestamp = 0

    def empty(self):
        return self.dogs.empty() and self.cats.empty()

    def __len__(self):
        return len(self.dogs) + len(self.cats)

    def enqueue(self, animal):
        if animal.typeof(AnimalType.DOG):
            self.dogs.add((animal.name, self.timestamp))
        else:
            self.cats.add((animal.name, self.timestamp))
        self.timestamp += 1

    def dequeue_any(self):
        if self.empty():
            raise Exception("No animals available")
        if self.dogs.empty():
            return self.dequeue_cat()
        elif self.cats.empty():
            return self.dequeue_dog()
        _, t1 = self.dogs.peek()
        _, t2 = self.cats.peek()
        if t1 < t2:
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()

    def dequeue_dog(self):
        if self.dogs.empty():
            raise Exception("No dogs available")
        return self.dogs.remove()[0]
    
    def dequeue_cat(self):
        if self.cats.empty():
            raise Exception("No casts available")
        return self.cats.remove()[0]

class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def typeof(self, type):
        return self.type is type

    def __str__(self):
        return f"{self.name} ({self.type.name})"

from enum import Enum
class AnimalType(Enum):
    DOG = 1
    CAT = 2


animals = [
    Animal('Whisker', AnimalType.CAT),
    Animal('Doggy', AnimalType.DOG),
    Animal('Douglass', AnimalType.DOG),
    Animal('Pirate', AnimalType.CAT),
    Animal('Meow', AnimalType.CAT),
    Animal('Woo', AnimalType.DOG),
]
shelter = AnimalShelter()
for animal in animals:
    shelter.enqueue(animal)
print(shelter.dequeue_any())
print(shelter.dequeue_cat())
print(shelter.dequeue_dog())
print(shelter.dequeue_cat())

print("----" * 4)
shelter = AnimalShelter2()
for animal in animals:
    shelter.enqueue(animal)
print(shelter.dequeue_any())
print(shelter.dequeue_cat())
print(shelter.dequeue_dog())
print(shelter.dequeue_cat())