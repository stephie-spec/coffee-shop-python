class Coffee:
    all_coffees = []
    
    def __init__(self, name):
        self.name = name
        self._orders = []
        Coffee.all_coffees.append(self)
    
    def orders(self):
        return self._orders
    
    def customers(self):
        customer_list = []
        for order in self._orders:
            if order.customer not in customer_list:
                customer_list.append(order.customer)
        return customer_list
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if not self._orders:
            return 0
        
        total = 0
        for order in self._orders:
            total += order.price
        
        return total / len(self._orders)