class Order:
    all_orders = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        customer.order_list.append(self)
        coffee.order_list.append(self)
        Order.all_orders.append(self)