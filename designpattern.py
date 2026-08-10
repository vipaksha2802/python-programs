# Base class
class Pizza:
    def prepare(self):
        print("Preparing pizza...")


# Concrete classes
class Margherita(Pizza):
    def prepare(self):
        print("Preparing Margherita Pizza")


class Farmhouse(Pizza):
    def prepare(self):
        print("Preparing Farmhouse Pizza")


class Pepperoni(Pizza):
    def prepare(self):
        print("Preparing Pepperoni Pizza")


# Factory class
class PizzaFactory:
    @staticmethod
    def get_pizza(pizza_type):
        if pizza_type == "margherita":
            return Margherita()
        elif pizza_type == "farmhouse":
            return Farmhouse()
        elif pizza_type == "pepperoni":
            return Pepperoni()
        else:
            return None


# Client code
pizza_type = input("Enter pizza type: ").lower()

pizza = PizzaFactory.get_pizza(pizza_type)

if pizza:
    pizza.prepare()
else:
    print("Pizza not available")