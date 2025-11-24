from customer import Customer
from coffee import Coffee
from order import Order

def main():
    print("COFFEE SHOP ORDERS")
    # Create customers
    mary = Customer("Mary")
    joe = Customer("Joe")
    sarah = Customer("Sarah")
    
    # Create coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    cappuccino = Coffee("Cappuccino")
    
    # Create orders
    Order(mary, latte, 4.0)
    Order(mary, espresso, 3.5)
    
    Order(joe, cappuccino, 5.0)
    Order(joe, latte, 4.0)
    
    Order(sarah, cappuccino, 5.0)
    Order(sarah, cappuccino, 5.0)
    
    # Display customer orders
    customers = [mary, joe, sarah]
    
    for customer in customers:
        print(f"{customer.name}'s Orders:")
        for order in customer.orders:
            print(f"  - {order.coffee.name}: ${order.price}")
    

    print("\nCOFFEE STATISTICS")
    coffees = [latte, espresso, cappuccino]
    for coffee in coffees:
        print(f"{coffee.name}:")
        print(f"  Orders: {coffee.num_orders()}")
        print(f"  Avg Price: ${coffee.average_price():.1f}")
        print(f"  Customers: {len(coffee.customers())}")
    

    print("\nMOST AFICIONADO")    
    for coffee in coffees:
        aficionado = Customer.most_aficionado(coffee)
        if aficionado:
            total = sum(order.price for order in aficionado.orders 
                       if order.coffee == coffee)
            print(f"{coffee.name}: {aficionado.name} (${total})")

if __name__ == "__main__":
    main()