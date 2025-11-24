class Order:
    all_orders = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        customer.orders.append(self)
        coffee.orders.append(self)
        Order.all_orders.append(self)