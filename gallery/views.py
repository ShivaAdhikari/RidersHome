from django.shortcuts import render

# Create your views here.
def show_gallery(request):
    return render(request,'gallery.html')