
#Task One
class Policyholder:

    # constructor method to be used to create instances of the class
    def __init__(self, name: str, account_number: str):
        self.name = name
        self.account_number = account_number
        self.products = []
        self.payments = []
        self.is_active = True

    # str builtin method overridden to ensure better format when printed.
    def __str__(self):
        return f"Name: {self.name} \nAccount Number: {self.account_number}\nProducts Purchased: {len(self.products)}\n\n"
    """
    Task Two
       - Method for registration
       - Method for suspension
       - Method for reactivation  
    """
    # The register method register an existing policyholder to a new product
    # It adds the product object to the products property which is a list of product
    # It also adds the payment object to the payments property which is a list of payments
    # made by the policyholder
    def register(self, product, payment):
        self.products.append(product)
        self.payments.append(payment)

    # The suspend method changes the policyholder's active status to false
    def suspend(self):
        self.is_active = False

    # The reactivate method changes the policyholder's active status to true.
    # It basically reactivates the policyholder's account
    def reactivate(self):
        self.is_active = True