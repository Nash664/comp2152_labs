from mammal import Mammal
from tick import Tick

class Puma(Mammal):
    def __init__(self, age, tick):
        super().__init__(age)
        self.tick = tick

    def speak(self):
        print("Rawr")
    
    def __str__(self):
        return f"Puma, aged {self.age}, with a heart that beats at {self.heart}. It has a tick attached."
    
    def interact_with_tick(self):
        self.tick.suck_blood() 