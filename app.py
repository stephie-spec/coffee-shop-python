from customer import Customer
from coffee import Coffee
from order import Order

def main():
    print("WELCOME TO THE COFFEE SHOP!\n")
    
    # Create customers
    mary = Customer("Mary")
    joe = Customer("Joe")
    
    # Create coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    cappuccino = Coffee("Cappuccino")
    
    # Create orders
    Order(mary, latte, 400)
    Order(mary, espresso, 450)
    Order(joe, cappuccino, 450)
    Order(joe, latte, 400)
    
    # Show customer info
    print("CUSTOMER ORDERS")
    for customer in [mary, joe]:
        print(f"\n{customer.name}'s Orders:")
        for order in customer.orders():
            print(f"  - {order.coffee.name}: Ksh{order.price}")
    
    # Show coffee info
    print("\n COFFEE INFO")
    for coffee in [latte, espresso, cappuccino]:
        print(f"\n{coffee.name}:")
        print(f"  Orders: {coffee.num_orders()}")
        print(f"  Avg Price: Ksh{coffee.average_price():.1f}")
        print(f"  Customers: {[c.name for c in coffee.customers()]}")
    
    # Find biggest coffee aficionado
    print("\nCOFFEE AFICIONADO")
    latte_aficionado = Customer.most_aficionado(latte)
    if latte_aficionado:
        print(f"Biggest latte aficionado: {latte_aficionado.name}")

if __name__ == "__main__":
    main()