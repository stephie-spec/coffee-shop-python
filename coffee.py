class Coffee:
    all_coffees = []
    
    def __init__(self, name):
        self.name = name
        self.orders = []
        Coffee.all_coffees.append(self)
    
    def get_orders(self):
        return self.orders
    
    def get_customers(self):
        unique_customers = []
        for order in self.orders:
            if order.customer not in unique_customers:
                unique_customers.append(order.customer)
        return unique_customers
    
    def num_orders(self):
        return len(self.orders)
    
    def average_price(self):
        if not self.orders:
            return 0
        
        total = 0
        for order in self.orders:
            total += order.price
        
        return total / len(self.orders)