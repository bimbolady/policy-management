#Task One
class Product:

    # constructor method to be used to create instances of the class
    # This is considered the create method in this case
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        self.is_active = True

    # str builtin method overridden to ensure better format when printed.
    def __str__(self):
        return f"Product name: {self.name}\nProduct price: {self.price}\nProduct Active: {self.is_active}\n\n"

    # del builtin method overridden to ensure that the product
    # is deleted once the code has finished running
    def __del__(self):
        print(f"Product with name {self.name} has been deleted")

    """
    Task Two - 
       - Method for creation
       - Method for updating
       - Method for removing
       - Method for suspending 
    """

    # def create(self, name: str, price: float):
    #     product = Product(name, price)
    #     return product

    # This method alters the properties of the product
    # The name can be changed, the price can be changed and the active status can also be inverted
    def update(self, name: str = None, price: float = None, is_active: bool = None):
        if name is not None:
            self.name = name

        if price is not None:
            self.price = price

        if is_active is not None:
            self.is_active = is_active

    # This method calls the delete method which is used to remove the object from the code entirely
    def remove(self):
        del self

    # This alters the is_active property of the product from true to false
    def suspend(self):
        self.is_active = False
