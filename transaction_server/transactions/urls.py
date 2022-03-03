from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('workload', views.workload, name='workload'),
	path('create_user/<slug:userid>/', views.create_user),
	path('add/<slug:userid>/<int:amount>/', views.add),
	path('buy/<slug:userid>/<slug:stock_symbol>/<int:amount>/', views.buy),
	path('commit_buy/<slug:userid>/', views.commit_buy),
	path('cancel_buy/<slug:userid>/', views.cancel_buy),
	path('sell/<slug:userid>/<slug:stock_symbol>/<int:amount>/', views.sell),
	path('commit_sell/<slug:userid>/', views.commit_sell),
	path('cancel_sell/<slug:userid>/', views.cancel_sell),
	path('set_buy_amount/<slug:userid>/<slug:stock_symbol>/<int:amount>/', views.set_buy_amount),
	path('set_buy_trigger/<slug:userid>/<slug:stock_symbol>/<int:amount>/', views.set_buy_trigger),
	path('cancel_set_buy/<slug:userid>/<slug:stock_symbol>/', views.cancel_set_buy),
	path('set_sell_amount/<slug:userid>/<slug:stock_symbol>/<int:amount>/', views.set_sell_amount),
	path('set_sell_trigger/<slug:userid>/<slug:stock_symbol>/<int:amount>/', views.set_sell_trigger),
	path('cancel_sell_buy/<slug:userid>/<slug:stock_symbol>/', views.cancel_set_sell)
]
