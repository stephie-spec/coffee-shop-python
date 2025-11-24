class Coffee:
    all_coffees = []
    
    def __init__(self, name):
        self.name = name
        self.order_list = []
        Coffee.all_coffees.append(self)
    
    def get_orders(self):
        return self.order_list
    
    def get_customers(self):
        unique_customers = []
        for order in self.order_list:
            if order.customer not in unique_customers:
                unique_customers.append(order.customer)
        return unique_customers
    
    def num_orders(self):
        return len(self.order_list)
    
    def average_price(self):
        if not self.order_list:
            return 0
        
        total = 0
        for order in self.order_list:
            total += order.price
        
        return total / len(self.order_list)