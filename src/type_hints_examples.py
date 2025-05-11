# Without type hints
def without_calculate_total(price, quantity, tax_rate):
    return price * quantity * (1 + tax_rate)

# With type hints
def with_calculate_total(price: float, quantity: int, tax_rate: float) -> float:
    return price * quantity * (1 + tax_rate)

print(f"Without Type Hints:",without_calculate_total(10, 2, 0.1))
print(f"With Type Hints:",with_calculate_total(10, 2, 0.1))

# Without type hints - this error is invisible until runtime
def without_apply_discount(price, discount):
    return price * (1 - discount)

# Someone might call it like this, causing a runtime error
without_total_price = without_apply_discount(100, "15%")  # Oops!

# With type hints
def with_apply_discount(price: float, discount: float) -> float:
    return price * (1 - discount)

# Tools like mypy would catch this error during development
with_total_price = with_apply_discount(100, "15%")  # Type error!

print(f"Without Type Hints:{without_total_price}")
print(f"With Type Hints:{with_total_price}")