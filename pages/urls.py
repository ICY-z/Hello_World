from django.urls import path
from pages.views import homeView
from pages.views import aboutView
from pages.views import contactView
from pages.views import cartView , include

urlpattrens = [
    path('home/', homeView.as_view()),
    path('about/', aboutView.as_view()),
    path('contact/',contactView.as_view()),
    path('cart/',cartView.as_view()),
    path('',include('pages.urls'))
]