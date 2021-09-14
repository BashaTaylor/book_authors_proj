class Product:
    def __init__(self, prodName, price, category):
        self.prodName = prodName
        self.price = price
        self.category = category
    def print_info(self):
        print(f"Product name is{self.prodName}{self.price}{self.category}")
        
