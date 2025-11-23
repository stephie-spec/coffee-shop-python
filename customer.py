class Customer:
    all_customers = []
    
    def __init__(self, name):
        self.name = name
        self._orders = []
        Customer.all_customers.append(self)
    
    def orders(self):
        return self._orders
    
    def coffees(self):
        coffee_list = []
        for order in self._orders:
            if order.coffee not in coffee_list:
                coffee_list.append(order.coffee)
        return coffee_list
    
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        return order
    
    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None
        
        best_customer = None
        highest_spent = 0
        
        for customer in cls.all_customers:
            total = 0
            for order in customer.orders():
                if order.coffee == coffee:
                    total += order.price
            
            if total > highest_spent:
                highest_spent = total
                best_customer = customer
        
        return best_customer