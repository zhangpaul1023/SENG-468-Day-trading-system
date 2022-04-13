from django.urls import path, re_path

from . import views

urlpatterns = [
 #    path('', views.index, name='index'),
	# path('workload', views.workload, name='workload'),

	path('create_user/<slug:userid>/', views.create_user),
	re_path(r'^add/(?P<userid>[A-Za-z0-9_]+)/(?P<amount>\d*\.\d\d)/$', views.add),
	path('quote/<slug:userid>/<slug:stock_symbol>/', views.quote),
	re_path(r'^buy/(?P<userid>[A-Za-z0-9_]+)/(?P<stock_symbol>[A-Z]{1,3})/(?P<amount>\d*\.\d\d)/$', views.buy),
	path('commit_buy/<slug:userid>/', views.commit_buy),
	path('cancel_buy/<slug:userid>/', views.cancel_buy),
	re_path(r'^sell/(?P<userid>[A-Za-z0-9_]+)/(?P<stock_symbol>[A-Z]{1,3})/(?P<amount>\d*\.\d\d)/$', views.sell),
	path('commit_sell/<slug:userid>/', views.commit_sell),
	path('cancel_sell/<slug:userid>/', views.cancel_sell),
	re_path(r'^set_buy_amount/(?P<userid>[A-Za-z0-9_]+)/(?P<stock_symbol>[A-Z]{1,3})/(?P<amount>\d*\.\d\d)/$', views.set_buy_amount),
	re_path(r'^set_buy_trigger/(?P<userid>[A-Za-z0-9_]+)/(?P<stock_symbol>[A-Z]{1,3})/(?P<amount>\d*\.\d\d)/$', views.set_buy_trigger),
	path('cancel_set_buy/<slug:userid>/<slug:stock_symbol>/', views.cancel_set_buy),
	re_path(r'^set_sell_amount/(?P<userid>[A-Za-z0-9_]+)/(?P<stock_symbol>[A-Z]{1,3})/(?P<amount>\d*\.\d\d)/$', views.set_sell_amount),
	re_path(r'^set_sell_trigger/(?P<userid>[A-Za-z0-9_]+)/(?P<stock_symbol>[A-Z]{1,3})/(?P<amount>\d*\.\d\d)/$', views.set_sell_trigger),
	path('cancel_set_sell/<slug:userid>/<slug:stock_symbol>/', views.cancel_set_sell),
        path('dumplog/', views.dumplog)
]
