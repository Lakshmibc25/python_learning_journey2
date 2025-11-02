from currency_converter import CurrencyConverter
c = CurrencyConverter()

amt = float(input("\nenter amount in USD:"))

new_amt = (c.convert(amt,"USD" ,"INR"))

print(f"amount in INR :{new_amt}")
