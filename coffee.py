class Coffee:
    all_coffees = []
    
    def __init__(self, name):
        self.coffee_name = name
        self.orders = [] 
        Coffee.all_coffees.append(self)
    
    @property
    def name(self):
        return self.coffee_name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self.coffee_name = value
    
    def get_orders(self):
        return self.orders
    
    def get_customers(self):
        return list({order.customer for order in self.orders})
    
    def num_orders(self):
        return len(self.orders)
    
    def average_price(self):
        if not self.orders:
            return 0
        total = sum(order.price for order in self.orders)
        return total / len(self.orders)
    
    def add_order(self, order):
        if order not in self.orders:
            self.orders.append(order)