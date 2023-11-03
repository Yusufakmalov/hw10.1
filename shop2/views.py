from django.shortcuts import render
from shop2.forms import FormModelForm
from django.http import HttpResponse
# Create your views here.
# def home_page(request):
#     return HttpResponse('<h1>Hello<h1/>')
from shop2.models import ProductModel
from django.views.generic import ListView


def index_page(request):
    products = ProductModel.objects.all().filter(title__icontains='Iphone')

    return render(request, 'index.html' )

def shop_page(request):
    products = ProductModel.objects.all().order_by()
    return render(request, 'shop.html', {'products: shop2'})

def index_html(request):
    return render(request, 'index.html')

# def article_page(request):
#     return render(request, 'article.html')
# def login_page(request):
#     return render(request, 'login.html')
#
# class index(ListView):
#     template_name = 'bases.html'
#     queryset = ProductModel.objects.all()
#     context_object_name = 'Shop2'

def send_form(request):
    context = {}


    form = FormModelForm(request.POST)
    if form.is_valid():
        form.save()


    context['form'] = form
    return render(request, 'forms.html', context)