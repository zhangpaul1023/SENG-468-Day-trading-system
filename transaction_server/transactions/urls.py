from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('workload', views.workload, name='workload'),
    path('add', views.workload, name='add'),
    path('buy', views.workload, name='buy'),
    path('sell', views.workload, name='sell'),
    path('commit_buy', views.workload, name='commit_buy'),
    path('cancel_buy', views.workload, name='cancel_buy'),
    path('commit_sell', views.workload, name='commit_sell'),
    path('cancel_sell', views.workload, name='cancel_sell'),
    path('set_buy_amount', views.workload, name='set_buy_amount'),
    path('set_sell_amount', views.workload, name='set_sell_amount'),
    path('cancel_set_buy', views.workload, name='cancel_set_buy'),
    path('set_buy_trigger', views.workload, name='set_buy_trigger'),
    path('set_sell_trigger', views.workload, name='set_sell_trigger'),
    path('cancel_set_sell', views.workload, name='cancel_set_sell'),
    path('dumplog', views.workload, name='dumplog'),
    path('display_summary', views.workload, name='display_summary'),
    path('quote', views.workload, name='quote')

]
