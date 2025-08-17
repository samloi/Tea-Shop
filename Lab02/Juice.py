from Drink import Drink

class Juice(Drink):
    def __init__(self, size, price, ingredients):
        super().__init__(size, price)
        self.ingredients = ingredients

    def info(self):
        price_str = "${:.2f}".format(self.price)
        return f"{'/'.join(self.ingredients)} Juice, {super().info()}"
    
