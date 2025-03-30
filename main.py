
from mammal import Mammal
from person import Person
from puma import Puma
from tick import Tick


print("=== Mammal Demo ===")
generic_mammal = Mammal(5)
print(generic_mammal)
generic_mammal.speak()
    
print("\n=== Person Demo ===")
person = Person("Alice", 30, 165)
person.heart.beat()  
print(person)
person.speak()
    
print("\n=== Tick Demo ===")
tick = Tick()
tick.suck_blood()
    
print("\n=== Puma Demo ===")
attached_tick = Tick()
puma = Puma(age=3, tick=attached_tick)
print(puma)
puma.speak()
puma.tick.suck_blood()
