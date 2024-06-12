class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name: str, pet_type: str, owner=None):
        """Initialize a new pet with a name, type, and optional owner."""
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(
                f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}"
            )
        self.name = name
        self.pet_type = pet_type
        self._owner = None
        if owner is not None:
            self.owner = owner
        Pet.all.append(self)

    @property
    def owner(self):
        """Get the owner of the pet."""
        return self._owner

    @owner.setter
    def owner(self, value):
        """Set the owner of the pet. Must be an instance of Owner."""
        if not isinstance(value, Owner):
            raise TypeError("Owner must be an instance of Owner class")
        self._owner = value

    @classmethod
    def validate_pet_type(cls, pet_type: str):
        """Validate the pet type. Must be one of the predefined PET_TYPES."""
        if pet_type not in cls.PET_TYPES:
            raise ValueError(
                f"Invalid pet type: {pet_type}. Must be one of {cls.PET_TYPES}"
            )
        return pet_type


class Owner:
    def __init__(self, name: str):
        """Initialize a new owner with a name."""
        self.name = name

    def pets(self):
        """Return a list of pets owned by this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet: Pet):
        """Add a pet to this owner. Pet must be an instance of Pet."""
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        """Return a list of pets owned by this owner, sorted by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)
