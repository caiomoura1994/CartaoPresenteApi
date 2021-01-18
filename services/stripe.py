from contents.models import Product

import stripe
from datetime import datetime
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


def handle_with_stripe_errors(e):
    error_message = None
    try:
        print(f'e.http_status: {e.http_status}')
        print(f'e.code: {e.code}')
        print(f'e.param: {e.param}')
        print(f'e.user_message: {e.user_message}')
        error_message = f"{e.user_message} - {e.code}"
    except:
        raise ValidationError('Erro não identificado')
    if e.param == 'phone':
        error_message = "Número de telefone inválido"
    if e.code == 'account_number_invalid':
        error_message = "Número de IBAN inválido"
    if e.code == 'postal_code_invalid':
        error_message = "Código postal inválido"
    if e.code == 'incorrect_number':
        error_message = "O número do cartão está incorreto."
    if e.code == 'invalid_number':
        error_message = "O número do cartão não é um número válido de cartão de crédito."
    if e.code == 'invalid_expiry_month':
        error_message = "O mês de validade do cartão não é válido."
    if e.code == 'invalid_expiry_year':
        error_message = "O ano de validade do cartão não é válido."
    if e.code == 'invalid_cvc':
        error_message = "O código de segurança do cartão não é válido."
    if e.code == 'expired_card':
        error_message = "O cartão expirou."
    if e.code == 'incorrect_cvc':
        error_message = "O código de segurança do cartão está incorreto."
    if e.code == 'incorrect_zip':
        error_message = "O CEP do cartão falhou a validação."
    if e.code == 'card_declined':
        error_message = "O cartão foi recusado."
    if e.code == 'missing':
        error_message = "Não existe qualquer cartão em um cliente que está sendo cobrado."
    if e.code == 'processing_error':
        error_message = "Ocorreu um erro durante o processamento do cartão."
    if not error_message or error_message == "None":
        error_message = f"Erro nao identificado {e.code}-{e.user_message}"

    raise ValidationError(error_message)

def create_checkout_session(product, amount, domain_url):
    try:
        return stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
            'price_data': {
                'currency': 'brl',
                'product_data': {
                    'name': f'{product.pk} - {product.name}'
                    # 'images': [product.images]
                },
                'unit_amount': amount,
            },
            'quantity': 1,
            }],
            mode='payment',
            success_url=domain_url + '/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain_url + f'/{product.slug}',
        )
    except Exception as e:
        return handle_with_stripe_errors(e)