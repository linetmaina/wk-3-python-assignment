def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If discount is 20% or higher, apply it; otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)
    print(f"The final price is: {final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values.")
