# sandwich_maker.py

class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when the order can be made, False if ingredients are insufficient."""
        for item, amount_required in ingredients.items():
            if item not in self.machine_resources or self.machine_resources[item] < amount_required:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deducts the required ingredients from resources and prints a confirmation."""
        if self.check_resources(order_ingredients):
            # Deduct the ingredients from resources
            for item, amount in order_ingredients.items():
                self.machine_resources[item] -= amount
            print(f"Your {sandwich_size} sandwich is ready!")
        else:
            print("Could not make the sandwich due to insufficient resources.")
