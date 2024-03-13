from django.urls import path
from .views import *

app_name = 'siterifa'

urlpatterns = [
    path('', homepage, name='home'),
    path('rifa/<int:rifa_id>/', comprar, name='shop'),
    path('finalizar_pagamento/', finalizar_pagamento, name='finalizar_pagamento'),
    path('pix/', pix, name='pix')
]
