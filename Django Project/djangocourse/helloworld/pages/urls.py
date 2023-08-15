from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView,ProductIndexView, ProductShowView, Product


urlpatterns = [
    path("",HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path ('contact/', ContactPageView.as_view(), name= 'contact'),
    path('pages/products/', ProductIndexView.as_view(), name='index'),
    path('pages/products/<str:id>', ProductShowView.as_view(), name='show'),

]