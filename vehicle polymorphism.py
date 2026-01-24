class BMW:
    """Represents a BMW car."""

    def __init__(self, model):
        self.model = model

    def sound(self):
        """Prints the characteristic sound of a BMW."""
        print(f"The {self.model} goes 'Vrooom'!")


class Ferrari:
    """Represents a Ferrari car."""

    def __init__(self, model):
        self.model = model

    def sound(self):
        """Prints the characteristic sound of a Ferrari."""
        print(f"The {self.model} goes 'Rumble Rumble'!")


# Create instances of both classes
car1 = BMW("M4")
car2 = Ferrari("488")
car3 = BMW("X5")

# Demonstrate polymorphism
for car in [car1, car2, car3]:
    car.sound()
