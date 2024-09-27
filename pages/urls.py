from django.urls import path
from pages.views import HomeView
from pages.views import aboutView
# from pages.views import contactView
# from pages.views import cartView , include

urlpatterns = [
    path('', HomeView.as_view()),
    path('about/', aboutView),
    # path('contact/',contactView),
    # path('cart/',cartView),
]