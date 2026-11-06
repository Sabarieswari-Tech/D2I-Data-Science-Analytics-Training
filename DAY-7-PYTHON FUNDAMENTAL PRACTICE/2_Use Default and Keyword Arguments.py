def calculate_bill(prices, tax_rate=0.10, discount=0.20):
    subtotal = sum(prices)
    discount_amount = subtotal * discount
    discounted_price = subtotal - discount_amount
    tax = discounted_price * tax_rate
    total = discounted_price + tax

    print(f"Subtotal: {subtotal:.2f}")
    print(f"Discount: {discount_amount:.2f}")
    print(f"Tax: {tax:.2f}")
    print(f"Final total: {total:.2f}")


prices = [100, 50]
calculate_bill(prices, tax_rate=0.10, discount=0.20)