class Order:
    all_orders = []
    
    def __init__(self, customer, coffee, price):
        if not isinstance(price, float) or not 1.0 <= price <= 10.0:
            raise Exception("Price must be float between 1.0-10.0")
        
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        customer.orders.append(self)
        coffee.orders.append(self)
        Order.all_orders.append(self)