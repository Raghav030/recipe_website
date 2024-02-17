from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    peoples=[{'name': 'a', 'age': 12},
             {'name': 'b', 'age': 15},
             {'name': 'c', 'age': 32}
             ]
    return render(request, "home/index.html", context={'peoples': peoples})
def success_page(request):
    print ("*"*10)
    return HttpResponse("this is the success page")
def about(request):
    # print ("*"*10)
    context={'page': 'about'}
    return render(request, 'home/about.html', context)
def contact(request):
    context={'page': 'contact'}
    return render(request, 'home/contact.html', context)
    