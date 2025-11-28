class Customer:
    all_customers = []
    
    def __init__(self, name):
        self.customer_name = name
        self.orders = [] 
        Customer.all_customers.append(self)
    
    @property
    def name(self):
        return self.customer_name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self.customer_name = value
    
    def get_orders(self):
        return self.orders
    
    def get_coffees(self):
        return list({order.coffee for order in self.orders})
    
    def create_order(self, coffee, price):
        from order import Order
        new_order = Order(self, coffee, price)
        return new_order
    
    def add_order(self, order):
        if order not in self.orders:
            self.orders.append(order)
    
    @classmethod
    def most_aficionado(cls, coffee):
        best_customer = None
        highest_spent = 0
        
        for customer in cls.all_customers:
            total = 0
            for order in customer.get_orders():  
                if order.coffee == coffee:
                    total += order.price
            
            if total > highest_spent:
                highest_spent = total
                best_customer = customer
        
        return best_customer