class Customer:
    all_customers = []
    
    def __init__(self, name):
        if not isinstance(name, str) or not 1 <= len(name) <= 15:
            raise Exception("Name must be string between 1-15 characters")
        self.name = name
        self.orders = []
        Customer.all_customers.append(self)
    
    def create_order(self, coffee, price):
        from order import Order
        new_order = Order(self, coffee, price)
        return new_order
    
    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders:
            return None
        
        best_customer = None
        highest_spent = 0
        
        for customer in cls.all_customers:
            total = 0
            for order in customer.orders:
                if order.coffee == coffee:
                    total += order.price
            
            if total > highest_spent:
                highest_spent = total
                best_customer = customer
        
        return best_customer