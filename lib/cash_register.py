#!/usr/bin/env python3

class CashRegister:
  
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, item_cost):
        self.items.append(item_cost)
        self.total += item_cost
        self.last_transaction = item_cost

    def apply_discount(self):
        if self.discount != 0:
            discount_amount = (self.discount / 100.0) * self.total
            self.total -= discount_amount
            return f"After applying a {self.discount}% discount, the total is: ${self.total:.2f}"
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        if self.last_transaction != 0:
            self.total -= self.last_transaction
            self.items.pop()
            self.last_transaction = 0
        else:
            return "No transaction to void."

# Test the CashRegister class
register = CashRegister(discount=10)
register.add_item(20)
register.add_item(30)
print(register.total)  # Output: 50
print(register.apply_discount())  # Output: "After applying a 10% discount, the total is: $45.00"
register.void_last_transaction()
print(register.total)  # Output: 20

