from Product import Product
from Policyholder import Policyholder
import random


# Task One
class Payment:

    # constructor method to be used to create instances of the class
    def __init__(self, amount: float, product: Product, policy_holder: Policyholder):
        self.amount = amount
        self.product = product
        self.policy_holder = policy_holder
        self.receipt_number = generate_receipt_number()

    # str builtin method overridden to ensure better format when printed.
    def __str__(self):
        return (f"---Payment Receipt--- \nAmount: {self.amount} \nPayee Number: {self.policy_holder.account_number} \n"
                f"Payee Name: {self.policy_holder.name} \n"
                f"Product: {self.product.name} \n"
                f"Receipt Number: {self.receipt_number}\n\n")

    """
     Task Two
        - Method for payment processing
        - Method for payment reminders
        - Method for payment penalties
    """

    # process is a static method because it is used to generate and process payment receipt.
    # It utilizes the __init__ constructor method to create an instance of payment
    # and then returns that instance
    @staticmethod
    def process(product: Product, policy_holder: Policyholder):
        # payment is processed by first creating an instance of payment class
        # and returning it
        payment = Payment(product.price, product, policy_holder)
        # The register method of the Policyholder class is called to ensure that
        # the product and payment records are stored in the policyholder record.
        policy_holder.register(product, payment)
        return payment

    # remind method
    # It does not return anything
    def remind(self):
        print(f"Hello, {self.policy_holder.name}, kindly make payment for your product")

    # penalties method.
    # It adds the penalty fee to the payment amount property
    def penalties(self, penalty_fee: float):
        self.amount += penalty_fee


# friend method used to generate receipt number for payment object
def generate_receipt_number():
    alphabet = list(map(chr, range(97, 123)))
    # number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    random_result = ""
    for i in range(0, 10):
        random_result += alphabet[random.randint(0, len(alphabet) - 1)]
        random_result += str(random.randint(0, 10))
    return random_result
