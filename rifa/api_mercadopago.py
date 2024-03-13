import mercadopago

public_key = "APP_USR-2e9f3793-6109-4199-b800-fd2e19682b57"
token = "APP_USR-6286399198507460-031209-98e5fa3a9893e5f81da181ef5ec24a48-286182413"


def create_payment(rifa_id, link):
    # Configure as credenciais
    sdk = mercadopago.SDK(token)
    # Crie um item na preferência

    # itens que ele está comprando no formato de dicionário
    itens = []
    itens.append({
            "title": "RIFA N° {}".format(rifa_id),
            "quantity": 1,
            "unit_price": 10,
        })

    # valor total
    preference_data = {
        "items": itens,
        "auto_return": "all",
        "back_urls": {
            "success": link,
            "pending": link,
            "failure": link,
        }
    }
    resposta = sdk.preference().create(preference_data)
    link_pagamento = resposta["response"]["init_point"]
    id_pagamento = resposta["response"]["id"]
    return link_pagamento, id_pagamento