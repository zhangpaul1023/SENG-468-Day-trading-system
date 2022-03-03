from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('workload', views.workload, name='workload'),
	path('create_user/<slug:userid>/', views.create_user),
	path('add/<slug:userid>/<int:amount>/', views.add),
	path('buy/<slug:userid>/<slug:stock_symbol>/<int:amount>/', views.buy),
	path('commit_buy/<slug:userid>/', views.commit_buy),
	path('cancel_buy/<slug:userid>/', views.cancel_buy)
]
