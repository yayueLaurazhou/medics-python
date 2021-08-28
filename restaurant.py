class Restaurant:
    # pass
    def __init__(self, customer_waiting, is_open, name):
        self.name = name.title()
        self.customer_waiting = customer_waiting
        self.is_open = is_open

    def open_restaurant(self):
        self.is_open = True
        print(self.name + "is open! Come and visit!")

    def get_customer_number(self):
        print(str(self.customer_waiting) + " customers are waiting to be served!")
        # return self.customer_waiting
        #

    def update_customer_number(self, number):
        self.customer_waiting = number


class PizzaPlace(Restaurant):
    def __init__(self, customer_waiting, is_open, name='PizzaHub'):
        super().__init__(customer_waiting, is_open, 'PizzaHub')
        self.menu = {
            "Margherita": {"flour": 250, "water": 100, "tomatoes": 300, "cheese": 300, "oil": 50, "salt": 5},
            "Pepperoni": {"flour": 250, "water": 100, "pepperoni": 200, "cheese": 200, "oil": 50, "salt": 5},
            "Vegan": {"flour": 250, "water": 100, "mushrooms": 200, "cheese": 200, "oil": 50, "salt": 5, "basil": 10,
                      "onion": 50}
        }

        self.resources = {
            "flour": 1000,
            "water": 100000,
            "tomatoes": 1000,
            "pepperoni": 1000,
            "cheese": 10000,
            "salt": 200,
            "basil": 100,
            "onion": 500,
            "oil": 500,
            "mushrooms": 500
        }

    def get_menu(self):
        for key in self.menu:
            print(key)

    def report_resources(self):
        # Prints a report of all resources."""
        print(f"flour: {self.resources['flour']}g")
        print(f"water: {self.resources['water']}g")
        print(f"tomatoes: {self.resources['tomatoes']}g")
        print(f"pepperoni: {self.resources['pepperoni']}g")
        print(f"cheese: {self.resources['cheese']}g")
        print(f"salt: {self.resources['salt']}g")
        print(f"basil: {self.resources['basil']}g")
        print(f"onion: {self.resources['onion']}g")
        print(f"oil: {self.resources['oil']}g")
        print(f"mushrooms: {self.resources['mushrooms']}g")

    def is_resource_sufficient(self, pizza_name):
        # Returns True when order can be made, False if ingredients are insufficient.
        can_make = True
        for item in self.menu[pizza_name]:
            if self.menu[pizza_name][item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_pizza(self, order):
        if self.is_resource_sufficient(order):
            for item in self.menu[order]:
                self.resources[item] -= self.menu[order][item]
        self.customer_waiting -= 1


restaurant1 = Restaurant(5, False, "Sushimania")
restaurant1.open_restaurant()
restaurant1.update_customer_number(20)
restaurant1.customer_waiting = 20
restaurant1.get_customer_number()
print("\n")

pizza_place1 = PizzaPlace(3, False)
pizza_place1.get_menu()
pizza_place1.make_pizza("Pepperoni")
pizza_place1.get_customer_number()
