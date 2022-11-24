from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name="index"),
    path('<int:month>' , views.monthly_challenge_by_number),   # dynamic url handling
    path('<str:month>',views.monthly_challenge , name="monthly_challenge")# yaha tak k url ko name dediya taki dynamic use kr sake
]
