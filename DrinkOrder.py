class DrinkOrder:
    def __init__(self):
        self.drinks = []

    def add(self, drink):
        self.drinks.append(drink)

    def total(self):
        items = ""
        total_price = 0
        for drink in self.drinks:
            items = items + f"* {drink.info()}\n"
            total_price = total_price + drink.get_price()

        return f"Order Items:\n{items}Total Price: ${total_price:.2f}"
