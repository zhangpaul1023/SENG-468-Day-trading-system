from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(UncommittedBuy)
admin.site.register(UncommittedSell)
admin.site.register(StockAccount)
admin.site.register(BuyTrigger)
admin.site.register(SellTrigger)


