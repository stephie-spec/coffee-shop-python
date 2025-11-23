class Order:
    all_orders = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        # Connect to customer and coffee
        customer._orders.append(self)
        coffee._orders.append(self)
        Order.all_orders.append(self)