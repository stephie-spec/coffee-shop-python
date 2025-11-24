class Customer:
    all_customers = []
    
    def __init__(self, name):
        self.name = name
        self.orders = []
        Customer.all_customers.append(self)
    
    def get_orders(self):
        return self.orders
    
    def get_coffees(self):
        unique_coffees = []
        for order in self.orders:
            if order.coffee not in unique_coffees:
                unique_coffees.append(order.coffee)
        return unique_coffees
    
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        return order
    
    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.get_orders():
            return None
        
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