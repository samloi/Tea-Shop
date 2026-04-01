class Drink:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    def get_size(self):
        return self.size

    def get_price(self):
        return self.price

    def update_size(self, new_size):
        self.size = new_size

    def update_price(self, new_price):
        self.price = new_price

    def info(self):
        return f"{self.size}: ${self.price:.2f}"
