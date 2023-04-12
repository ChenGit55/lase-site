import stripe
from decouple import config


STRIPE_SECRRET_KEY = config('STRIPE_SECRET_KEY')
STRIPE_PUBLISHABLE_KEY = config('STRIPE_PUBLIC_KEY')
STRIPE_CURRENCY = 'usd'

stripe.api_key = STRIPE_SECRRET_KEY