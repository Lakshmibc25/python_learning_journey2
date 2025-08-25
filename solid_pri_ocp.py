class product:
    def __init__(self, name,price):
        self.name = name
        self.price = price
    def get_tax(self):
        return 0
     
class food(product):
    def get_tax(self):
        return self.price * 0.05  # 5% tax
    
class electronics(product):
    def get_tax(self):
        return self.price * 0.18 # 18% tax
    
def print_bill (product):
        tax = product.get_tax()
        total = product.price + tax
        print(f"{product.name} - Price:{product.price} , Tax:{tax}, Total :{total}")

f = food("bread", 50)
e = electronics("tv", 20000)

print_bill(f)
print_bill(e)