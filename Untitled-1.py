class Mobile:
    def _init_(self, brand, price):
        self.brand = brand
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}, Price: ₹{self.price}")

# Creating two objects (Class name must be 'Mobile')
mobile1 = Mobile("Samsung", 15000)
mobile2 = Mobile("Apple", 80000)

# Displaying their attributes
mobile1.display_info()
mobile2.display_info()