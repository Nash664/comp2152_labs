class Person:

    def __init__(self, name, age,height):
        self._name = name
        self._age = age
        self._height = height
        self.public_prop="I am public"

        print("Constructing the Person Object")


    #def get_name(self):
     #   return self._name
    
   # def set_name(self, name):
    #    self._name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    def __del__(self):
        print(f"Deleting person object.")




person1=Person("Mark", 20, 6) 
   
print(person1.public_prop)

#print(person1.get_name())
#person1.set_name("Anna")
#print(person1.get_name())

print(person1.name)
person1.name="Anna"
print(person1.name)




