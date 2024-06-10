from Policyholder import Policyholder
from Product import Product
from Payment import Payment


# function to generate a payment.
# It accepts a product object and a policyholder object.

def generate_payment_record(product: Product, policy_holder: Policyholder):
    return Payment.process(product, policy_holder)


if __name__ == "__main__":
    # creation of the two policyholder instances with different names and account numbers
    policy_holder_1 = Policyholder("Michael Darent", "2393939301")
    policy_holder_2 = Policyholder("David Mauricio", "4040404004")

    # creation of the products namely car_insurance and healthcare_insurance
    car_insurance_product = Product("Gold Car Insurance", 95000)
    healthcare_insurance_product = Product("Healthcare insurance", 45000)

    # generation of payment for the policy holders.
    payment = generate_payment_record(car_insurance_product, policy_holder_1)
    payment2 = generate_payment_record(healthcare_insurance_product, policy_holder_2)
    payment3 = generate_payment_record(healthcare_insurance_product, policy_holder_1)

    # The __str__ method in the Policyholder class makes
    # it possible for us to print the policyholders account details
    # in a legible manner.
    print(policy_holder_1)
    print(policy_holder_2)

    # Changing the car insurance name to Normal car insurance using
    # Changing the car insurance product price to 90000
    # Changing the active status to false
    # the update method
    car_insurance_product.update("Normal Car Insurance", 90000, False)
    print(car_insurance_product)

