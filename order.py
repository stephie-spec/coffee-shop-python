class Order:
    all_orders = []
    
    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee
        
        if not isinstance(customer, Customer):
            raise ValueError("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be a Coffee instance")
        
        self.order_customer = customer
        self.order_coffee = coffee
        self.order_price = price
        
        customer.add_order(self)
        coffee.add_order(self)
        Order.all_orders.append(self)
    
    @property
    def customer(self):
        return self.order_customer
    
    @property
    def coffee(self):
        return self.order_coffee
    
    @property
    def price(self):
        return self.order_price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Price must be a number")
        
        price_float = float(value)
        if not 1.0 <= price_float <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        
        self.order_price = price_float