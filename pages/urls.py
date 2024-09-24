from django.urls import path
from pages.views import homeView
from pages.views import aboutView
from pages.views import contactView
from pages.views import cartView , include

urlpattrens = [
    path('home/', homeView.as_view()),
    path('about/', aboutView),
    path('contact/',contactView),
    path('cart/',cartView),
    path('',include('pages.urls'))
]