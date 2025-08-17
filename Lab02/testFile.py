from Drink import Drink 

class TestDrink:
    def test_init(self):
        drink = Drink('medium',20.5)
        assert drink.size == 'medium'
        assert drink.price == 20.5

    def test_get_size(self):
        drink = Drink ('large', 20.95)
        assert drink.get_size() == 'large'

    def test_get_price(self): 
        drink = Drink ('small', 10.15)
        assert drink.get_price() == 10.15

    def test_update_size(self):
        drink = Drink ('small', 10.15)
        drink.update_size('medium')
        assert drink.size == 'medium'

    def test_update_price(self):
        drink = Drink ('small' , 10.15)
        drink.update_price(12.75)
        assert drink.price == 12.75

    def test_info(self): 
        drink = Drink ('medium', 20.5)
        assert drink.info() == "medium: $20.50"


from Drink import Drink
from Tea import Tea
from Juice import Juice

class TestTea:
    def test_init(self):
        tea = Tea('small', 2.75, "Camomile")
        assert tea.size == 'small'
        assert tea.price == 2.75
        assert tea.style == 'Camomile'

    def test_info(self):
        tea = Tea('small' , 2.75, "Camomile")
        assert tea.info() == "Camomile Tea, small: $2.75"

class TestJuice: 
    def test_init(self):
        juice = Juice('large', 7.0, ["Blueberry", "Rasberry"])
        assert juice.size == 'large'
        assert juice.price == 7.0
        assert juice.ingredients == ["Blueberry", "Rasberry"]

    def test_info(self): 
        juice = Juice('large', 7.0, ["Blueberry", "Rasberry"])
        assert juice.info() == "Blueberry/Rasberry Juice, large: $7.00"



from Drink import Drink
from Tea import Tea
from Juice import Juice
from DrinkOrder import DrinkOrder

class TestDrinkOrder:
    def test_init(self):
        order = DrinkOrder()
        assert order.drinks == []
    
    def test_add(self):
        tea = Tea('small', 2.75, "Camomile")
        juice = Juice('large', 7.0, ["Blueberry", "Rasberry"])
        order = DrinkOrder()
        order.add(tea)
        order.add(juice)
        assert order.drinks == [tea, juice]

    def test_total(self):
        tea = Tea('small', 2.75, "Camomile")
        juice = Juice('large', 7.0, ["Blueberry", "Rasberry"])
        order = DrinkOrder()
        order.add(tea)
        order.add(juice)
        assert order.total() == (
            """Order Items:\n"""
            """* Camomile Tea, small: $2.75\n"""
            """* Blueberry/Rasberry Juice, large: $7.00\n"""
            """Total Price: $9.75"""  
        )


