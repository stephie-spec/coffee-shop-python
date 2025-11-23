# Coffee Shop

A simple Python application of a coffee shop.

## Setup

1. **Navigate to project directory:**
   ```bash
   cd coffee_shop
   ```

2. **Set up environment:**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

## Key Features

### Customer Class
- Track all orders placed by a customer
- See all unique coffees a customer has ordered
- Create new orders easily
- Find the biggest spender for any coffee

### Coffee Class  
- Count how many times a coffee has been ordered
- Calculate average price for a coffee
- See all customers who have ordered a coffee

### Order Class
- Connect customers to coffees with prices
- Automatic relationship management

## Example Output

```
WELCOME TO THE COFFEE SHOP!

CUSTOMER ORDERS:

Mary's Orders:
  - Latte: Ksh 400
  - Espresso: Ksh 450

Joe's Orders:
  - Cappuccino: kSH 450
  - Latte: Ksh 400

COFFEE INFO:

Latte:
  Orders: 2
  Avg Price: Ksh 500
  Customers: ['Mary', 'Joe']

COFFEE AFICIONADO:
Biggest latte aficionado: Mary
```


## Technology Stack

- **Python 3.11+** - Core programming language
- **Pipenv** - Dependency management


