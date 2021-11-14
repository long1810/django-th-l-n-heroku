from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect 
# Create your views here.
def index(request):
    # response = HttpResponse()
    # response.writelines('<h1> xin choa cac ban</h1>')
    # response.write('dau la home')
    # return response
    return render(request, 'pages/home.html')

def contact(request):
   return render(request, 'pages/contact.html')


def chon_hang(request):
   return render(request, 'pages/chon_hang.html')

def login(request):
   return render(request, 'pages/login.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})