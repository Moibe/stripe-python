# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = "sk_test_UEqlnnbMITO2SqRQ10ZJh33P"

linko = stripe.PaymentLink.create(line_items=[{"price": 'price_1PqffeIYi36CbmfWrVMF6z6l', "quantity": 1}])

print(linko)