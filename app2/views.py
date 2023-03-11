from django.shortcuts import render

# Create your views here.
def end(request):
    return render(request,"end.html")