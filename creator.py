import stripe

stripe.api_key = "sk_test_UEqlnnbMITO2SqRQ10ZJh33P"

#Aquí estamos creando un objeto que será nuestra suscripción.
starter_subscription = stripe.Product.create(
  name="Starter Subscription",
  description="$12/Month subscription",
)

#Y un precio
starter_subscription_price = stripe.Price.create(
  unit_amount=1200, #Mira como es representado el 12.
  currency="usd",
  recurring={"interval": "month"},
  product=starter_subscription['id'], #Aquí llamas al producto recién creado, es decir al crear el precio le puedes asignar un producto. ¿o siempre?
)

# Save these identifiers
print(f"Success! Here is your starter subscription product id: {starter_subscription.id}")
print(f"Success! Here is your starter subscription price id: {starter_subscription_price.id}")

stripe.PaymentLink.create(line_items=[{"price": 'price_1PqffeIYi36CbmfWrVMF6z6l', "quantity": 1}])