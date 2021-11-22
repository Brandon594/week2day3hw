class Cart:
    def __init__(self):
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self,item):
        self.cart_items.remove(item)
    def get_items(self):
        return self.cart_items



mycart = Cart()


def cart_program(cart):
    while True:
        response = input("(a)dd, (r)emove, or (v)iew cart?")
        if response == "a":
            item = input("what is your item?")
            cart.add_item(item)
            print(item, "added!")
        elif response == "r":
            item = input("what is your item?")
            cart.remove_item(item)
            print(item,"removed!")
        elif response == "v":
            print(cart.get_items())


cart_program(mycart)

