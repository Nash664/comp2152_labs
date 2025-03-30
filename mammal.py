from heart import Heart

class Mammal:
    def __init__(self, age):
        self.age = age
        self.heart = Heart()

    def speak(self):
        print("Generic mammal sound")

    def __str__(self):
        return f"A mammal aged {self.age} with a heart that beats at {self.heart}"    