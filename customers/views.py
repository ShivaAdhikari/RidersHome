from django.shortcuts import render

# Create your views here.
def show_customers(request):
    return render(request,'customers.html')