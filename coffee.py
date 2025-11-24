class Coffee:
    all_coffees = []
    
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise Exception("Name must be string at least 3 characters")
        self.name = name
        self.orders = []
        Coffee.all_coffees.append(self)
    
    def num_orders(self):
        return len(self.orders)
    
    def average_price(self):
        if not self.orders:
            return 0
        total = sum(order.price for order in self.orders)
        return total / len(self.orders)
    
    def customers(self):
        unique_customers = []
        for order in self.orders:
            if order.customer not in unique_customers:
                unique_customers.append(order.customer)
        return unique_customers