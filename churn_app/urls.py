from django.urls import path
from . import views

urlpatterns = [
    path('', views.churn_predict, name='churn_predict'),
    path('dashboard/', views.churn_dashboard, name='churn_dashboard'),
]