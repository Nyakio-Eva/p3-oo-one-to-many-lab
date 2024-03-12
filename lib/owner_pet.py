class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self,name,pet_type,owner=None) -> None:
        if self.check_pet_type(pet_type):
            self.name = name
            self.pet_type = pet_type
            self.owner = owner
            Pet.all.append(self)
        else:
            raise TypeError("Pet must be of PET_TYPES.")
    
    @classmethod
    def check_pet_type(cls,pet_type):
        return pet_type in cls.PET_TYPES

class Owner:
    def __init__(self,name) -> None:
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all]
    
    
    def add_pet(self,pet):
        if not isinstance(pet, Pet):
            raise TypeError("pet must must be in pet_type or an instance of Pet class")
        
        pet.owner = self

    def get_sorted_pets(self):
        if Pet.all:
            sorted_pets = sorted(Pet.all, key=lambda pet: pet.name)
        
            return sorted_pets