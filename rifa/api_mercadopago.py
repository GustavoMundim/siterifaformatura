import mercadopago

public_key = "TEST-2cb4e79a-a12f-4286-b708-572b4650e3a6"
token = "TEST-6244779549547304-011715-156e0551b52ade4d706a7687e9c700fb-144516549"
# public_key = "APP_USR-2e9f3793-6109-4199-b800-fd2e19682b57"
# token = "APP_USR-6286399198507460-031209-98e5fa3a9893e5f81da181ef5ec24a48-286182413"

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