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
        # Recupera as informações do formulário
        token = request.POST['stripeToken']
        amount = int(request.POST['amount'])
        description = request.POST['description']

        try:
            # Cria uma nova transação com o Stripe
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description=description,
                source=token
            )
        except stripe.error.CardError as e:
            # Trata o erro caso o cartão seja recusado
            return False, e

    return render(request, 'payments.html', {'stripepb' : STRIPE_PK})

def subscription_view(request):
    # Verifica se a solicitação é uma solicitação POST
    if request.method == "POST":
        # Coleta os dados de pagamento do formulário enviado
        token = request.POST.get("stripeToken")
        amount = request.POST.get("amount")

        # Cria uma nova cobrança usando o Stripe
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency="usd",
                description="Mensalidade",
                source=token,
            )
            return HttpResponse("Cobrança realizada com sucesso.")
        except stripe.error.CardError as e:
            # Trata erros de cartão inválido
            return HttpResponse("Erro ao processar a cobrança: " + str(e))
    else:
        # Renderiza o template com o formulário de cobrança
        return render(request, "subscription.html", {'stripepb' : STRIPE_PK})
