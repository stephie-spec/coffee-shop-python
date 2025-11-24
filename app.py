from customer import Customer
from coffee import Coffee
from order import Order

def main():
    print("WELCOME TO THE COFFEE SHOP!")
    
    mary = Customer("Mary")
    joe = Customer("Joe")
    
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    cappuccino = Coffee("Cappuccino")
    
    Order(mary, latte, 4.0)
    Order(mary, espresso, 4.5)
    Order(joe, cappuccino, 6.0)
    Order(joe, latte, 4.0)
    
    print("CUSTOMER ORDERS")
    for customer in [mary, joe]:
        print(f"{customer.name}'s Orders:")
        for order in customer.get_orders():  
            print(f"  - {order.coffee.name}: ${order.price}")
    
    print("COFFEE INFO")
    for coffee in [latte, espresso, cappuccino]:
        print(f"{coffee.name}:")
        print(f"  Orders: {coffee.num_orders()}")
        print(f"  Avg Price: ${coffee.average_price():.1f}")
        print(f"  Customers: {[c.name for c in coffee.get_customers()]}")  
    
    print("COFFEE AFICIONADO")
    latte_lover = Customer.most_aficionado(latte)
    if latte_lover:
        print(f"Biggest latte aficionado: {latte_lover.name}")

if __name__ == "__main__":
    main()