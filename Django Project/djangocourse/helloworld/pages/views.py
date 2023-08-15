from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View


# Create your views here.
class  HomePageView(TemplateView):
    template_name ='pages/home.html'	

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Santiago Toro Orozco",
        })

        return context
    
class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "Email": "toro10chato@hotmail.com",
            "Address": "calle 77d sur # 30-23, Sabaneta, Antioquia",
            "Cellphon": "3104203131",
        })

        return context


class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "Prices":"$ 500.000"},
        {"id":"2", "name":"iPhone", "description":"Best iPhone","Prices":"$ 1.000.000"},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast","Prices":"$ 400.000"},
        {"id":"4", "name":"Glasses", "description":"Best Glasses","Prices":"$ 200.000"}
    ]

class ProductIndexView(View):
    template_name = 'pages/products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] =  "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'pages/products/show.html'


    def get(self, request, id):
        viewData = {}
        product = Product.products[int(id)-1]
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] =  product["name"] + " - Product information"
        viewData["product"] = product

        return render(request, self.template_name, viewData)

