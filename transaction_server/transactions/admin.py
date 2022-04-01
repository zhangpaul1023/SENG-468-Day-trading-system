from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(UncommittedBuy)
admin.site.register(UncommittedSell)
admin.site.register(StockAccount)
admin.site.register(SetBuy)
admin.site.register(SetSell)
admin.site.register(UserCommandLog)
admin.site.register(QuoteServerLog)
admin.site.register(AccountTransactionLog)
admin.site.register(SystemEventLog)
admin.site.register(ErrorEventLog)



