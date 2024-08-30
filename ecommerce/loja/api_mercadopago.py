import mercadopago

public_key = "APP_USR-2b04dd5e-ca75-410b-9c77-2068a8d5ed26"
token = "APP_USR-2122173498292496-083011-0944f7326410064e9e2b2ebe48971afa-1967629391"

sdk = mercadopago.SDK(token)

request_options = mercadopago.config.RequestOptions()
request_options.custom_headers = {
    'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
}

payment_data = {
    "transaction_amount": 100,
    "token": "CARD_TOKEN",
    "description": "Payment description",
    "payment_method_id": 'visa',
    "installments": 1,
    "payer": {
        "email": 'test_user_123456@testuser.com'
    }
}
result = sdk.payment().create(payment_data, request_options)
payment = result["response"]

print(payment)