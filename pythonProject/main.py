import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of the SandwichMaker and Cashier classes
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)  # Pass resources to SandwichMaker
cashier_instance = Cashier()  # No arguments needed for Cashier


def main():
    # Main program loop
    is_on = True
    while is_on:
        print("\nWelcome to the Sandwich Maker!")
        choice = input("What size sandwich would you like? (small/medium/large): ").lower()

        if choice in recipes:
            # Get the recipe and cost for the chosen sandwich
            order_ingredients = recipes[choice]["ingredients"]
            sandwich_cost = recipes[choice]["cost"]

            # Check if the machine has enough resources to make the sandwich
            if sandwich_maker_instance.check_resources(order_ingredients):
                # Process the payment
                payment = cashier_instance.process_coins()

                # Check if the transaction is successful
                if cashier_instance.transaction_result(payment, sandwich_cost):
                    # Make the sandwich
                    sandwich_maker_instance.make_sandwich(choice, order_ingredients)
                else:
                    print("Transaction failed. Not enough money provided.")
            else:
                print("Not enough resources to make this sandwich.")
        else:
            print("Invalid option. Please choose between small, medium, or large.")

        # Ask if the user wants to continue
        is_on = input("Would you like to make another sandwich? (yes/no): ").lower() == "yes"


if __name__ == "__main__":
    main()
