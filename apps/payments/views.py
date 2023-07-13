from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import stripe_settings
import stripe

stripe.api_key = stripe_settings.STRIPE_SECRRET_KEY
STRIPE_PK = stripe_settings.STRIPE_PUBLISHABLE_KEY

@csrf_exempt
def payment_view(request):

    print(STRIPE_PK)
    if request.method == 'POST':
        # Recovery the form informations
        token = request.POST['stripeToken']
        amount = int(request.POST['amount'])
        description = request.POST['description']

        try:
            # Create a new transaction with Stripe
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description=description,
                source=token
            )
        except stripe.error.CardError as e:
            # Handle decline card erro
            return False, e

    return render(request, 'payments.html', {'stripepb' : STRIPE_PK})

def subscription_view(request):
    # Checks if the request is a request
    if request.method == "POST":
        # Collects payment data from the submitted form
        token = request.POST.get("stripeToken")
        amount = request.POST.get("amount")

        # Create a new charge using Stripe
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency="usd",
                description="Mensalidade",
                source=token,
            )
            return render(request, "successfully-enrolled.html",{})
        except stripe.error.CardError as e:
            # Handle invalid card erros
            return HttpResponse("Error processing billing: " + str(e))
    else:
        # Renders the template with the billing form
        return render(request, "subscription.html", {'stripepb' : STRIPE_PK})
    
def successfully_enrolled_view(request):
    return render(request, "successfuly-enrolled.html",{})
