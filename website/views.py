from django.shortcuts import render,redirect
from .models import Product, Stock, Rents
from django.contrib.auth.decorators import login_required
from .forms import ContactFormForm,CustomUserForm
from django.contrib.auth import authenticate,login

# Create your views here.
#---------------productos------------
def product_list(request):
    tipo_prod = request.GET.get('tipoprod')
    products = Product.objects.filter(tipoprod=tipo_prod)
   

    return render(request, 'product_list.html', {'products': products})

#---------------carrito------------
def rent_list(request):
    items = Stock.objects.all()   

    return render(request, 'arriendo.html', {'items': items})

def delete_item(request):
    return True

def add_item(request):
    nombre = request.POST.get('nombre')
    precio = request.POST.get('precio')
    data = {'nombre':nombre, 'precio':precio, 'cantidad':1 }
    data.save()

    return render(request, 'arriendo.html',data)

#--------------carrito2----------------
def carrito(request):
    return render(request, 'carrito.html')

#--------------index-------------

def index(request):
    return render(request, 'index.html')

#----------------login------------------
def register(request):
    data = {
        'form': CustomUserForm()
    }
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            # Autenticar al usuario y redirigir al login
            usuario = form.cleaned_data["username"]
            contraseña = form.cleaned_data["password1"] 
            user = authenticate(request, username=usuario, password=contraseña)
            if user is not None and user.is_authenticated:
                login(request, user)
                return redirect('login')
        
    return render(request, 'registration/register.html', data)

@login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'login.html')

def logout_view(request):
    context = {}
    return render(request, 'index.html', context)

#------------------contacto---------------
def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            # Aquí puedes enviar notificaciones por correo electrónico si deseas
            return redirect('contact_success')
    else:
        form = ContactFormForm()
    
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')


#----------------terminmos soporte y privacidad-----------------------

def soporte(request):
    return render(request, 'soporte.html')
