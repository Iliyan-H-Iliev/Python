class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        prod = [p for p in self.products if p.name == product_name]
        if prod:
            return prod[0]

    def remove(self, product_name):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        result = '\n'.join(f"{x.name}: {x.quantity}" for x in self.products)

        return result
